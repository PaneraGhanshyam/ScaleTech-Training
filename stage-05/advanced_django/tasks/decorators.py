"""
Custom Decorators
=================
Decorators wrap views to add cross-cutting concerns like
permission checks, logging, and response modification.

Learning Points:
1. Function decorators using functools.wraps
2. Decorators with arguments (decorator factories)
3. Class-based view compatible decorators using method_decorator
"""

import functools
import logging
import time

from django.http import JsonResponse

logger = logging.getLogger("tasks.decorators")


# ---------------------------------------------------------------------------
# 1) @log_api_call — Logs entry/exit of any view function
# ---------------------------------------------------------------------------
def log_api_call(view_func):
    """
    Decorator that logs when an API view is called and how long it took.

    Usage:
        @log_api_call
        def my_view(request):
            ...

    HOW IT WORKS:
    - functools.wraps preserves the original function's name and docstring
    - We measure time before and after calling the actual view
    """

    @functools.wraps(view_func)
    def wrapper(request, *args, **kwargs):
        logger.info(
            "→ API call: %s %s (view=%s)",
            request.method,
            request.path,
            view_func.__name__,
        )
        start = time.time()
        response = view_func(request, *args, **kwargs)
        duration = (time.time() - start) * 1000
        logger.info(
            "← API response: %s %s → %s (%.1fms)",
            request.method,
            request.path,
            response.status_code,
            duration,
        )
        return response

    return wrapper


# ---------------------------------------------------------------------------
# 2) @require_owner — Ensures the user owns the object they're accessing
# ---------------------------------------------------------------------------
def require_task_owner(view_func):
    """
    Decorator that checks if the current user is the owner of the task.
    Expects `task_id` or `pk` in the URL kwargs.

    Usage:
        @require_task_owner
        def my_view(request, pk):
            ...
    """
    from .models import Task  # Lazy import to avoid circular imports

    @functools.wraps(view_func)
    def wrapper(request, *args, **kwargs):
        task_id = kwargs.get("pk") or kwargs.get("task_id")
        if task_id is None:
            return JsonResponse({"error": "No task ID provided"}, status=400)

        try:
            task = Task.objects.get(pk=task_id)
        except Task.DoesNotExist:
            return JsonResponse({"error": "Task not found"}, status=404)

        if task.owner != request.user:
            return JsonResponse(
                {"error": "You are not the owner of this task"}, status=403
            )

        # Attach the task to request so the view doesn't need to re-fetch
        request.task = task
        return view_func(request, *args, **kwargs)

    return wrapper


# ---------------------------------------------------------------------------
# 3) @role_required — Decorator factory (decorator with arguments)
# ---------------------------------------------------------------------------
def role_required(*required_groups):
    """
    Decorator factory that checks if the user belongs to any of the
    specified groups.

    Usage:
        @role_required("admin", "manager")
        def my_view(request):
            ...

    HOW IT WORKS:
    - This is a function that RETURNS a decorator
    - The outer function captures the arguments
    - The inner function is the actual decorator
    """

    def decorator(view_func):
        @functools.wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return JsonResponse(
                    {"error": "Authentication required"}, status=401
                )

            user_groups = set(
                request.user.groups.values_list("name", flat=True)
            )

            if not user_groups.intersection(required_groups):
                return JsonResponse(
                    {
                        "error": "Insufficient permissions",
                        "required_groups": list(required_groups),
                        "your_groups": list(user_groups),
                    },
                    status=403,
                )

            return view_func(request, *args, **kwargs)

        return wrapper

    return decorator


# ---------------------------------------------------------------------------
# 4) @cache_response — Simple response caching decorator
# ---------------------------------------------------------------------------
def cache_response(timeout=60):
    """
    Decorator factory that caches the response for GET requests.

    Usage:
        @cache_response(timeout=300)
        def my_view(request):
            ...

    NOTE: Only caches GET requests. POST/PUT/DELETE bypass the cache.
    """
    from django.core.cache import cache

    def decorator(view_func):
        @functools.wraps(view_func)
        def wrapper(request, *args, **kwargs):
            # Only cache GET requests
            if request.method != "GET":
                return view_func(request, *args, **kwargs)

            # Build a cache key from the view name and query string
            cache_key = f"view_cache:{view_func.__name__}:{request.get_full_path()}"
            cached = cache.get(cache_key)
            if cached is not None:
                logger.info("Cache HIT: %s", cache_key)
                return cached

            logger.info("Cache MISS: %s", cache_key)
            response = view_func(request, *args, **kwargs)
            cache.set(cache_key, response, timeout)
            return response

        return wrapper

    return decorator
