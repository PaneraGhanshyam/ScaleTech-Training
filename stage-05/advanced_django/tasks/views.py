"""
Views demonstrating ALL advanced concepts:
1. Authentication (Token, JWT, OAuth2) — already wired up
2. Middleware effects — visible via X-Request-Duration-Ms header
3. Custom decorators — @log_api_call, @require_task_owner, @cache_response
4. Signals — fire automatically on save/delete (see signals.py)
5. Caching — Django's cache framework
6. File upload — multipart form data handling
"""

import os
import logging

from django.core.cache import cache
from django.http import FileResponse, Http404
from django.utils.decorators import method_decorator

from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from oauth2_provider.contrib.rest_framework import (
    OAuth2Authentication,
    TokenHasScope,
)

from .decorators import log_api_call, cache_response
from .models import Task, TaskAttachment
from .serializers import (
    TaskSerializer,
    TaskCreateSerializer,
    TaskAttachmentSerializer,
    TaskAttachmentUploadSerializer,
)

logger = logging.getLogger("tasks.views")


# ===========================================================================
# AUTHENTICATION VIEWS (Token, JWT, OAuth2 already configured in urls.py)
# ===========================================================================

class CurrentUserView(APIView):
    """
    Returns the current authenticated user's info.
    Works with ALL three auth methods: Token, JWT, and OAuth2.

    Test with:
      - Token:  curl -H "Authorization: Token <token>" /api/me/
      - JWT:    curl -H "Authorization: Bearer <jwt>" /api/me/
      - OAuth2: curl -H "Authorization: Bearer <oauth_token>" /api/me/
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        auth_type = type(request.auth).__name__ if request.auth else "Session"
        return Response({
            "id": request.user.id,
            "username": request.user.username,
            "email": request.user.email,
            "auth_type": auth_type,
            "auth_backend": request.successful_authenticator.__class__.__name__
            if hasattr(request, "successful_authenticator")
            and request.successful_authenticator
            else "Unknown",
        })


class OAuthTaskListView(APIView):
    """
    OAuth2-only endpoint. Requires 'read' scope.
    Demonstrates scope-based access control.
    """
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasScope]
    required_scopes = ["read"]

    def get(self, request):
        tasks = (
            Task.objects
            .select_related("owner")
            .order_by("-created_at")
        )
        serializer = TaskSerializer(tasks, many=True)
        return Response({
            "count": tasks.count(),
            "results": serializer.data,
        })


# ===========================================================================
# TASK CRUD VIEWS — With Caching and Decorator examples
# ===========================================================================

class TaskListCreateView(APIView):
    """
    GET  /api/tasks/ — List all tasks (with caching)
    POST /api/tasks/ — Create a new task (triggers post_save signal)
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        List tasks with caching.

        CACHING EXPLAINED:
        - We check if "task_list_all" exists in cache
        - If YES → return cached data (fast!)
        - If NO → query DB, serialize, store in cache, return
        - Cache auto-invalidates when any task is saved/deleted (via signals)
        """
        cached_data = cache.get("task_list_all")
        if cached_data is not None:
            logger.info("Cache HIT for task list")
            return Response(cached_data)

        logger.info("Cache MISS for task list — querying DB")
        tasks = (
            Task.objects
            .select_related("owner")
            .prefetch_related("attachments")
            .order_by("-created_at")
        )
        serializer = TaskSerializer(tasks, many=True)
        response_data = {
            "count": tasks.count(),
            "results": serializer.data,
        }

        # Cache for 5 minutes (300 seconds)
        cache.set("task_list_all", response_data, 300)

        return Response(response_data)

    def post(self, request):
        """
        Create a new task.
        This triggers the post_save signal in signals.py.
        """
        serializer = TaskCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # owner is auto-set from the authenticated user
        task = serializer.save(owner=request.user)

        # Return the full representation
        return Response(
            TaskSerializer(task).data,
            status=status.HTTP_201_CREATED,
        )


class TaskDetailView(APIView):
    """
    GET    /api/tasks/<pk>/ — Retrieve a task (with per-task caching)
    PUT    /api/tasks/<pk>/ — Update a task (only owner)
    DELETE /api/tasks/<pk>/ — Delete a task (only owner, triggers post_delete signal)
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        """Retrieve with per-task caching."""
        cache_key = f"task_detail_{pk}"
        cached = cache.get(cache_key)
        if cached:
            return Response(cached)

        task = self._get_task_or_404(pk)
        data = TaskSerializer(task).data
        cache.set(cache_key, data, 300)
        return Response(data)

    def put(self, request, pk):
        """
        Update a task. Only the owner can update.
        Changing status will fire the custom task_status_changed signal.
        """
        task = self._get_task_or_404(pk)
        if task.owner != request.user:
            return Response(
                {"error": "Only the task owner can update this task"},
                status=status.HTTP_403_FORBIDDEN,
            )

        serializer = TaskCreateSerializer(task, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(TaskSerializer(task).data)

    def delete(self, request, pk):
        """
        Delete a task. This triggers post_delete signal.
        Attachments are cascade-deleted, and django-cleanup removes the files.
        """
        task = self._get_task_or_404(pk)
        if task.owner != request.user:
            return Response(
                {"error": "Only the task owner can delete this task"},
                status=status.HTTP_403_FORBIDDEN,
            )

        task.delete()  # Triggers post_delete signal!
        return Response(status=status.HTTP_204_NO_CONTENT)

    def _get_task_or_404(self, pk):
        try:
            return Task.objects.select_related("owner").get(pk=pk)
        except Task.DoesNotExist:
            raise Http404("Task not found")


# ===========================================================================
# FILE UPLOAD VIEWS
# ===========================================================================

class TaskAttachmentListView(APIView):
    """
    GET  /api/tasks/<task_id>/attachments/ — List all attachments for a task
    POST /api/tasks/<task_id>/attachments/ — Upload a new file attachment

    FILE UPLOAD EXPLAINED:
    - MultiPartParser handles multipart/form-data (files + form fields)
    - FormParser handles regular form data
    - The uploaded file is accessible via request.FILES
    """
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request, task_id):
        """List all attachments for a task."""
        attachments = TaskAttachment.objects.filter(
            task_id=task_id
        ).select_related("uploaded_by")
        serializer = TaskAttachmentSerializer(attachments, many=True)
        return Response({
            "count": attachments.count(),
            "results": serializer.data,
        })

    def post(self, request, task_id):
        """
        Upload a file to a task.

        HOW FILE UPLOAD WORKS:
        1. Client sends multipart/form-data with 'file' field
        2. Django puts uploaded files in request.FILES
        3. We validate with serializer
        4. FileField.save() writes to MEDIA_ROOT/attachments/YYYY/MM/DD/
        5. We store metadata (name, size, content_type) in the DB
        """
        # Verify the task exists
        try:
            task = Task.objects.get(pk=task_id)
        except Task.DoesNotExist:
            return Response(
                {"error": "Task not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        # Validate the upload
        upload_serializer = TaskAttachmentUploadSerializer(data=request.data)
        upload_serializer.is_valid(raise_exception=True)

        uploaded_file = upload_serializer.validated_data["file"]
        thumbnail = upload_serializer.validated_data.get("thumbnail")

        # Create the attachment with auto-populated metadata
        attachment = TaskAttachment.objects.create(
            task=task,
            file=uploaded_file,
            thumbnail=thumbnail,
            original_filename=uploaded_file.name,
            file_size=uploaded_file.size,
            content_type=getattr(
                uploaded_file, "content_type", "application/octet-stream"
            ),
            uploaded_by=request.user,
        )

        serializer = TaskAttachmentSerializer(attachment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TaskAttachmentDetailView(APIView):
    """
    GET    /api/attachments/<pk>/          — Get attachment metadata
    DELETE /api/attachments/<pk>/          — Delete attachment
    GET    /api/attachments/<pk>/download/ — Download the actual file
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        """Get attachment metadata."""
        attachment = self._get_attachment_or_404(pk)
        return Response(TaskAttachmentSerializer(attachment).data)

    def delete(self, request, pk):
        """
        Delete an attachment.
        django-cleanup automatically removes the file from disk.
        """
        attachment = self._get_attachment_or_404(pk)
        if attachment.uploaded_by != request.user:
            return Response(
                {"error": "Only the uploader can delete this attachment"},
                status=status.HTTP_403_FORBIDDEN,
            )

        attachment.delete()  # django-cleanup handles file removal
        return Response(status=status.HTTP_204_NO_CONTENT)

    def _get_attachment_or_404(self, pk):
        try:
            return TaskAttachment.objects.select_related(
                "uploaded_by", "task"
            ).get(pk=pk)
        except TaskAttachment.DoesNotExist:
            raise Http404("Attachment not found")


class AttachmentDownloadView(APIView):
    """
    Download the actual file (binary response).

    FILERESPONSE EXPLAINED:
    - FileResponse streams the file efficiently (doesn't load entire file into memory)
    - Content-Disposition header tells the browser to download vs. display
    - as_attachment=True forces download instead of inline display
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            attachment = TaskAttachment.objects.get(pk=pk)
        except TaskAttachment.DoesNotExist:
            raise Http404("Attachment not found")

        if not attachment.file:
            return Response(
                {"error": "No file associated with this attachment"},
                status=status.HTTP_404_NOT_FOUND,
            )

        response = FileResponse(
            attachment.file.open("rb"),
            content_type=attachment.content_type or "application/octet-stream",
            as_attachment=True,
            filename=attachment.original_filename,
        )
        return response


# ===========================================================================
# CACHING DEMO VIEW — Demonstrates various caching strategies
# ===========================================================================

class CacheDemoView(APIView):
    """
    GET /api/cache-demo/ — Shows different caching strategies

    CACHING STRATEGIES:
    1. cache.get/set — Basic key-value caching
    2. cache.get_or_set — Atomic get-or-create
    3. cache.incr/decr — Atomic counter operations
    4. cache.set_many/get_many — Bulk operations
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Strategy 1: Basic get/set
        basic_value = cache.get("demo_basic")
        if basic_value is None:
            basic_value = "This was just computed!"
            cache.set("demo_basic", basic_value, timeout=30)
            basic_source = "computed"
        else:
            basic_source = "cached"

        # Strategy 2: get_or_set (atomic — avoids race conditions)
        atomic_value = cache.get_or_set(
            "demo_atomic",
            lambda: f"Computed at request time for user {request.user.username}",
            timeout=30,
        )

        # Strategy 3: Atomic counters
        view_count_key = "demo_view_count"
        try:
            view_count = cache.incr(view_count_key)
        except ValueError:
            cache.set(view_count_key, 1, timeout=300)
            view_count = 1

        # Strategy 4: Bulk operations
        cache.set_many(
            {
                "demo_bulk_1": "value1",
                "demo_bulk_2": "value2",
                "demo_bulk_3": "value3",
            },
            timeout=30,
        )
        bulk_values = cache.get_many(
            ["demo_bulk_1", "demo_bulk_2", "demo_bulk_3"]
        )

        return Response({
            "basic_cache": {
                "value": basic_value,
                "source": basic_source,
                "hint": "Refresh within 30s to see 'cached'",
            },
            "atomic_cache": {
                "value": atomic_value,
                "hint": "Uses get_or_set to avoid race conditions",
            },
            "counter": {
                "view_count": view_count,
                "hint": "Increments atomically on each request",
            },
            "bulk_cache": {
                "values": bulk_values,
                "hint": "Set and retrieved 3 keys in one operation",
            },
        })

    def delete(self, request):
        """Clear all demo cache keys."""
        cache.delete_many([
            "demo_basic",
            "demo_atomic",
            "demo_view_count",
            "demo_bulk_1",
            "demo_bulk_2",
            "demo_bulk_3",
        ])
        return Response({"message": "All demo cache keys cleared"})