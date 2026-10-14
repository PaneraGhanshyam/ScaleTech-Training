"""
Custom Middleware Examples
=========================
Middleware runs on EVERY request/response cycle.
Order in MIDDLEWARE list matters — top-to-bottom for requests, bottom-to-top for responses.

Learning Points:
1. __init__  → called once when the server starts
2. __call__ → called on every request
3. process_view / process_exception → optional hooks
"""

import time
import logging
from collections import defaultdict

from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger("tasks.middleware")


# ---------------------------------------------------------------------------
# 1) Request Logging Middleware (function-based style)
# ---------------------------------------------------------------------------
class RequestLoggingMiddleware:
    """
    Logs every request with method, path, user, and response time.

    HOW IT WORKS:
    - Captures start time before the view runs
    - Captures end time after the response is returned
    - Logs the difference as "response_time_ms"
    """

    def __init__(self, get_response):
        # Called once at server start — get_response is the next middleware or the view
        self.get_response = get_response

    def __call__(self, request):
        # ----- BEFORE the view -----
        start = time.time()
        request.start_time = start  # Attach to request for decorators to use

        # Call the next middleware / view
        response = self.get_response(request)

        # ----- AFTER the view -----
        duration_ms = (time.time() - start) * 1000

        logger.info(
            "%(method)s %(path)s → %(status)s (%(duration).1fms) [user=%(user)s]",
            {
                "method": request.method,
                "path": request.path,
                "status": response.status_code,
                "duration": duration_ms,
                "user": getattr(request, "user", "anonymous"),
            },
        )

        # You can also add custom headers to every response
        response["X-Request-Duration-Ms"] = f"{duration_ms:.1f}"

        return response


# ---------------------------------------------------------------------------
# 2) Simple Rate-Limiting Middleware (class-based with MiddlewareMixin)
# ---------------------------------------------------------------------------
class SimpleRateLimitMiddleware(MiddlewareMixin):
    """
    Limits each IP to MAX_REQUESTS_PER_WINDOW requests within WINDOW_SECONDS.

    NOTE: This uses an in-memory dict, so it resets on server restart and
    doesn't work across multiple processes. For production, use Redis.

    HOW IT WORKS:
    - Tracks request timestamps per IP address
    - Removes expired timestamps outside the window
    - Returns 429 Too Many Requests if limit is exceeded
    """

    MAX_REQUESTS_PER_WINDOW = 100  # max requests
    WINDOW_SECONDS = 60            # per this many seconds

    # Class-level storage — shared across all requests
    _request_log = defaultdict(list)

    def process_request(self, request):
        """Called before the view. Return None to continue, or an HttpResponse to short-circuit."""
        ip = self._get_client_ip(request)
        now = time.time()
        window_start = now - self.WINDOW_SECONDS

        # Remove old entries outside the window
        self._request_log[ip] = [
            t for t in self._request_log[ip] if t > window_start
        ]

        if len(self._request_log[ip]) >= self.MAX_REQUESTS_PER_WINDOW:
            return JsonResponse(
                {
                    "error": "Rate limit exceeded",
                    "detail": f"Max {self.MAX_REQUESTS_PER_WINDOW} requests "
                              f"per {self.WINDOW_SECONDS}s",
                    "retry_after_seconds": self.WINDOW_SECONDS,
                },
                status=429,
            )

        self._request_log[ip].append(now)
        return None  # Continue to the view

    def process_response(self, request, response):
        """Add rate-limit headers to every response."""
        ip = self._get_client_ip(request)
        remaining = max(
            0,
            self.MAX_REQUESTS_PER_WINDOW - len(self._request_log.get(ip, [])),
        )
        response["X-RateLimit-Limit"] = str(self.MAX_REQUESTS_PER_WINDOW)
        response["X-RateLimit-Remaining"] = str(remaining)
        return response

    @staticmethod
    def _get_client_ip(request):
        """Extract client IP, handling reverse proxies."""
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            return x_forwarded_for.split(",")[0].strip()
        return request.META.get("REMOTE_ADDR", "unknown")
