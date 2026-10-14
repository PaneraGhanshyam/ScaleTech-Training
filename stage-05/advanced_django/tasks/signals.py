"""
Django Signals
==============
Signals allow decoupled applications to be notified when certain actions occur.
They implement the Observer Pattern — senders don't need to know about receivers.

Learning Points:
1. Built-in signals: pre_save, post_save, pre_delete, post_delete
2. Custom signals
3. Signal receivers with @receiver decorator
4. Connecting signals in AppConfig.ready()
"""

import logging

from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import Signal, receiver
from django.core.cache import cache

from .models import Task

logger = logging.getLogger("tasks.signals")


# ===========================================================================
# CUSTOM SIGNAL — Define your own signals for domain events
# ===========================================================================
# Custom signal that fires when a task's status changes
task_status_changed = Signal()  # Sends: sender, instance, old_status, new_status


# ===========================================================================
# SIGNAL RECEIVERS
# ===========================================================================

@receiver(pre_save, sender=Task)
def track_status_change(sender, instance, **kwargs):
    """
    pre_save fires BEFORE the model is saved to the database.
    We use it to detect status changes by comparing old vs new values.

    HOW IT WORKS:
    - If the task already exists (has pk), fetch the old version from DB
    - Compare old status with new status
    - If different, fire our custom task_status_changed signal
    """
    if instance.pk:
        try:
            old_task = Task.objects.get(pk=instance.pk)
            if old_task.status != instance.status:
                # Store old status on instance for post_save to use
                instance._old_status = old_task.status
                logger.info(
                    "Task '%s' status changing: %s → %s",
                    instance.title,
                    old_task.status,
                    instance.status,
                )
        except Task.DoesNotExist:
            pass
    else:
        instance._old_status = None


@receiver(post_save, sender=Task)
def on_task_saved(sender, instance, created, **kwargs):
    """
    post_save fires AFTER the model is saved to the database.

    Args:
        sender: The model class (Task)
        instance: The actual Task object that was saved
        created: True if a new record was created, False if updated
    """
    if created:
        logger.info(
            "✅ New task created: '%s' by user %s (id=%s)",
            instance.title,
            instance.owner,
            instance.pk,
        )
    else:
        logger.info(
            "📝 Task updated: '%s' (id=%s)",
            instance.title,
            instance.pk,
        )
        # Fire custom signal if status changed
        old_status = getattr(instance, "_old_status", None)
        if old_status and old_status != instance.status:
            task_status_changed.send(
                sender=Task,
                instance=instance,
                old_status=old_status,
                new_status=instance.status,
            )

    # Invalidate cache whenever a task is saved
    _invalidate_task_cache(instance)


@receiver(post_delete, sender=Task)
def on_task_deleted(sender, instance, **kwargs):
    """
    post_delete fires AFTER the model is deleted from the database.
    Great for cleanup tasks, logging, or notifications.
    """
    logger.info(
        "🗑️  Task deleted: '%s' (id=%s) by user %s",
        instance.title,
        instance.pk,
        instance.owner,
    )
    _invalidate_task_cache(instance)


@receiver(task_status_changed)
def handle_status_change(sender, instance, old_status, new_status, **kwargs):
    """
    Receiver for our CUSTOM signal.
    This could trigger notifications, update dashboards, etc.
    """
    logger.info(
        "🔔 STATUS CHANGE notification: Task '%s' moved from '%s' to '%s'",
        instance.title,
        old_status,
        new_status,
    )
    # In a real app, you might:
    # - Send an email notification
    # - Push a WebSocket message
    # - Update analytics counters
    # - Trigger a Celery task


# ===========================================================================
# CACHE INVALIDATION HELPERS
# ===========================================================================

def _invalidate_task_cache(task_instance):
    """
    Invalidate all cached task-related data when a task changes.
    This ensures cached API responses stay fresh.
    """
    # Delete task list cache
    cache.delete("task_list_all")
    cache.delete(f"task_detail_{task_instance.pk}")
    cache.delete(f"user_tasks_{task_instance.owner_id}")
    logger.debug("Cache invalidated for task id=%s", task_instance.pk)
