"""
Comprehensive Tests for ALL Advanced Django Concepts
====================================================
Tests cover:
1. Authentication (Token, JWT)
2. Middleware (request logging, rate limiting)
3. Custom Decorators
4. Signals (post_save, post_delete, custom signal)
5. Caching
6. File Upload & Management
"""

import io
import tempfile
from unittest.mock import patch

from django.contrib.auth.models import User
from django.core.cache import cache
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, RequestFactory, override_settings
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase

from tasks.decorators import log_api_call, require_task_owner, role_required
from tasks.middleware import RequestLoggingMiddleware, SimpleRateLimitMiddleware
from tasks.models import Task, TaskAttachment


# ===========================================================================
# 1. AUTHENTICATION TESTS
# ===========================================================================

class TokenAuthenticationTest(APITestCase):
    """Test DRF Token Authentication."""

    def setUp(self):
        self.user = User.objects.create_user(
            username="tokenuser", password="testpass123"
        )
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()

    def test_obtain_token(self):
        """POST /api/token/ should return a token for valid credentials."""
        response = self.client.post(
            "/api/token/",
            {"username": "tokenuser", "password": "testpass123"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("token", response.data)
        self.assertEqual(response.data["token"], self.token.key)

    def test_access_with_token(self):
        """Authenticated requests with Token should succeed."""
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")
        response = self.client.get("/api/me/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["username"], "tokenuser")
        self.assertEqual(response.data["auth_type"], "Token")

    def test_access_without_token(self):
        """Unauthenticated requests should be rejected."""
        response = self.client.get("/api/me/")
        self.assertEqual(response.status_code, 401)


class JWTAuthenticationTest(APITestCase):
    """Test JWT Authentication."""

    def setUp(self):
        self.user = User.objects.create_user(
            username="jwtuser", password="testpass123"
        )
        self.client = APIClient()

    def test_obtain_jwt_token(self):
        """POST /api/jwt/token/ should return access and refresh tokens."""
        response = self.client.post(
            "/api/jwt/token/",
            {"username": "jwtuser", "password": "testpass123"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_access_with_jwt(self):
        """Requests with valid JWT should succeed."""
        # Get tokens
        token_response = self.client.post(
            "/api/jwt/token/",
            {"username": "jwtuser", "password": "testpass123"},
        )
        access_token = token_response.data["access"]

        # Use access token
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
        response = self.client.get("/api/me/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["username"], "jwtuser")

    def test_refresh_jwt_token(self):
        """POST /api/jwt/token/refresh/ should return a new access token."""
        token_response = self.client.post(
            "/api/jwt/token/",
            {"username": "jwtuser", "password": "testpass123"},
        )
        refresh_token = token_response.data["refresh"]

        response = self.client.post(
            "/api/jwt/token/refresh/",
            {"refresh": refresh_token},
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("access", response.data)

    def test_verify_jwt_token(self):
        """POST /api/jwt/token/verify/ should validate a token."""
        token_response = self.client.post(
            "/api/jwt/token/",
            {"username": "jwtuser", "password": "testpass123"},
        )
        access_token = token_response.data["access"]

        response = self.client.post(
            "/api/jwt/token/verify/",
            {"token": access_token},
        )
        self.assertEqual(response.status_code, 200)


# ===========================================================================
# 2. MIDDLEWARE TESTS
# ===========================================================================

class RequestLoggingMiddlewareTest(TestCase):
    """Test the custom request logging middleware."""

    def setUp(self):
        self.user = User.objects.create_user(
            username="middlewareuser", password="testpass123"
        )
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Token {self.token.key}"
        )

    def test_response_has_duration_header(self):
        """Every response should have X-Request-Duration-Ms header."""
        response = self.client.get("/api/me/")
        self.assertIn("X-Request-Duration-Ms", response)
        # Should be a valid float
        duration = float(response["X-Request-Duration-Ms"])
        self.assertGreaterEqual(duration, 0)

    def test_logging_middleware_logs_request(self):
        """Middleware should log the request."""
        with patch("tasks.middleware.logger") as mock_logger:
            self.client.get("/api/me/")
            mock_logger.info.assert_called()


class RateLimitMiddlewareTest(TestCase):
    """Test the rate-limiting middleware."""

    def setUp(self):
        self.user = User.objects.create_user(
            username="ratelimituser", password="testpass123"
        )
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Token {self.token.key}"
        )
        # Reset the rate limit log between tests
        SimpleRateLimitMiddleware._request_log.clear()

    def test_rate_limit_headers_present(self):
        """Response should contain rate limit headers."""
        response = self.client.get("/api/me/")
        self.assertIn("X-RateLimit-Limit", response)
        self.assertIn("X-RateLimit-Remaining", response)

    def test_rate_limit_decrements(self):
        """Remaining count should decrease with each request."""
        r1 = self.client.get("/api/me/")
        r2 = self.client.get("/api/me/")
        remaining1 = int(r1["X-RateLimit-Remaining"])
        remaining2 = int(r2["X-RateLimit-Remaining"])
        self.assertEqual(remaining1 - 1, remaining2)

    @override_settings()
    def test_rate_limit_exceeded(self):
        """Should return 429 when rate limit is exceeded."""
        # Temporarily lower the limit
        original_limit = SimpleRateLimitMiddleware.MAX_REQUESTS_PER_WINDOW
        SimpleRateLimitMiddleware.MAX_REQUESTS_PER_WINDOW = 3
        SimpleRateLimitMiddleware._request_log.clear()

        try:
            for _ in range(3):
                self.client.get("/api/me/")

            response = self.client.get("/api/me/")
            self.assertEqual(response.status_code, 429)
            self.assertIn("Rate limit exceeded", response.json()["error"])
        finally:
            SimpleRateLimitMiddleware.MAX_REQUESTS_PER_WINDOW = original_limit
            SimpleRateLimitMiddleware._request_log.clear()


# ===========================================================================
# 3. DECORATOR TESTS
# ===========================================================================

class DecoratorTest(TestCase):
    """Test custom decorators."""

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username="decoratoruser", password="testpass123"
        )
        self.task = Task.objects.create(
            title="Decorator Test Task",
            owner=self.user,
        )

    def test_log_api_call_preserves_function(self):
        """@log_api_call should preserve the original function's name."""
        from django.http import HttpResponse

        @log_api_call
        def my_view(request):
            return HttpResponse("OK")

        self.assertEqual(my_view.__name__, "my_view")

    def test_log_api_call_passes_through(self):
        """@log_api_call should not alter the response."""
        from django.http import HttpResponse

        @log_api_call
        def my_view(request):
            return HttpResponse("test content")

        request = self.factory.get("/test/")
        response = my_view(request)
        self.assertEqual(response.content, b"test content")

    def test_require_task_owner_allows_owner(self):
        """@require_task_owner should allow the task owner."""
        from django.http import JsonResponse

        @require_task_owner
        def my_view(request, pk):
            return JsonResponse({"status": "ok"})

        request = self.factory.get("/test/")
        request.user = self.user
        response = my_view(request, pk=self.task.pk)
        self.assertEqual(response.status_code, 200)

    def test_require_task_owner_denies_non_owner(self):
        """@require_task_owner should deny a non-owner."""
        from django.http import JsonResponse

        other_user = User.objects.create_user(
            username="other", password="pass"
        )

        @require_task_owner
        def my_view(request, pk):
            return JsonResponse({"status": "ok"})

        request = self.factory.get("/test/")
        request.user = other_user
        response = my_view(request, pk=self.task.pk)
        self.assertEqual(response.status_code, 403)

    def test_require_task_owner_404_for_missing_task(self):
        """@require_task_owner should return 404 for non-existent task."""
        from django.http import JsonResponse

        @require_task_owner
        def my_view(request, pk):
            return JsonResponse({"status": "ok"})

        request = self.factory.get("/test/")
        request.user = self.user
        response = my_view(request, pk=99999)
        self.assertEqual(response.status_code, 404)


# ===========================================================================
# 4. SIGNAL TESTS
# ===========================================================================

class SignalTest(TestCase):
    """Test Django signals."""

    def setUp(self):
        self.user = User.objects.create_user(
            username="signaluser", password="testpass123"
        )

    def test_post_save_signal_fires_on_create(self):
        """Creating a task should trigger the post_save signal."""
        with patch("tasks.signals.logger") as mock_logger:
            Task.objects.create(title="Signal Test", owner=self.user)
            # Check that the creation was logged
            log_messages = [
                str(call) for call in mock_logger.info.call_args_list
            ]
            self.assertTrue(
                any("New task created" in msg for msg in log_messages),
                f"Expected 'New task created' in logs. Got: {log_messages}",
            )

    def test_post_save_signal_fires_on_update(self):
        """Updating a task should trigger the post_save signal."""
        task = Task.objects.create(title="Signal Test", owner=self.user)
        with patch("tasks.signals.logger") as mock_logger:
            task.title = "Updated Title"
            task.save()
            log_messages = [
                str(call) for call in mock_logger.info.call_args_list
            ]
            self.assertTrue(
                any("Task updated" in msg for msg in log_messages),
                f"Expected 'Task updated' in logs. Got: {log_messages}",
            )

    def test_custom_signal_fires_on_status_change(self):
        """Changing task status should fire the custom task_status_changed signal."""
        task = Task.objects.create(
            title="Status Signal Test",
            owner=self.user,
            status="todo",
        )
        with patch("tasks.signals.logger") as mock_logger:
            task.status = "done"
            task.save()
            log_messages = [
                str(call) for call in mock_logger.info.call_args_list
            ]
            self.assertTrue(
                any("STATUS CHANGE" in msg for msg in log_messages),
                f"Expected 'STATUS CHANGE' in logs. Got: {log_messages}",
            )

    def test_post_delete_signal_fires(self):
        """Deleting a task should trigger the post_delete signal."""
        task = Task.objects.create(title="Delete Signal", owner=self.user)
        with patch("tasks.signals.logger") as mock_logger:
            task.delete()
            log_messages = [
                str(call) for call in mock_logger.info.call_args_list
            ]
            self.assertTrue(
                any("Task deleted" in msg for msg in log_messages),
                f"Expected 'Task deleted' in logs. Got: {log_messages}",
            )

    def test_cache_invalidated_on_save(self):
        """Saving a task should invalidate the cache."""
        cache.set("task_list_all", {"cached": True})
        Task.objects.create(title="Cache Invalidation", owner=self.user)
        self.assertIsNone(cache.get("task_list_all"))


# ===========================================================================
# 5. CACHING TESTS
# ===========================================================================

class CachingTest(APITestCase):
    """Test caching behavior."""

    def setUp(self):
        self.user = User.objects.create_user(
            username="cacheuser", password="testpass123"
        )
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Token {self.token.key}"
        )
        cache.clear()

    def test_task_list_uses_cache(self):
        """Second request to task list should use cached data."""
        Task.objects.create(title="Cache Test", owner=self.user)

        # First request — cache miss
        r1 = self.client.get("/api/tasks/")
        self.assertEqual(r1.status_code, 200)

        # Verify data is now cached
        cached = cache.get("task_list_all")
        self.assertIsNotNone(cached)

        # Second request should return same data from cache
        r2 = self.client.get("/api/tasks/")
        self.assertEqual(r1.data, r2.data)

    def test_cache_invalidated_on_create(self):
        """Creating a task should invalidate the task list cache."""
        cache.set("task_list_all", {"old": "data"})

        self.client.post("/api/tasks/", {"title": "New Task"})
        self.assertIsNone(cache.get("task_list_all"))

    def test_cache_demo_endpoint(self):
        """Cache demo endpoint should work and show caching strategies."""
        response = self.client.get("/api/cache-demo/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("basic_cache", response.data)
        self.assertIn("counter", response.data)
        self.assertEqual(response.data["counter"]["view_count"], 1)

        # Second request should increment counter
        response2 = self.client.get("/api/cache-demo/")
        self.assertEqual(response2.data["counter"]["view_count"], 2)

    def test_cache_demo_clear(self):
        """DELETE /api/cache-demo/ should clear all demo cache keys."""
        self.client.get("/api/cache-demo/")  # Populate cache
        response = self.client.delete("/api/cache-demo/")
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(cache.get("demo_basic"))


# ===========================================================================
# 6. FILE UPLOAD & MANAGEMENT TESTS
# ===========================================================================

@override_settings(MEDIA_ROOT=tempfile.mkdtemp())
class FileUploadTest(APITestCase):
    """Test file upload and management."""

    def setUp(self):
        self.user = User.objects.create_user(
            username="uploaduser", password="testpass123"
        )
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Token {self.token.key}"
        )
        self.task = Task.objects.create(
            title="Upload Test Task", owner=self.user
        )

    def _create_test_file(self, name="test.txt", content=b"Hello World", content_type="text/plain"):
        """Helper to create a test file."""
        return SimpleUploadedFile(name, content, content_type=content_type)

    def test_upload_file(self):
        """Should upload a file and return attachment metadata."""
        test_file = self._create_test_file()
        response = self.client.post(
            f"/api/tasks/{self.task.pk}/attachments/",
            {"file": test_file},
            format="multipart",
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["original_filename"], "test.txt")
        self.assertEqual(response.data["file_size"], 11)
        self.assertEqual(response.data["uploaded_by"], "uploaduser")

    def test_upload_creates_attachment_record(self):
        """Upload should create a TaskAttachment in the database."""
        test_file = self._create_test_file()
        self.client.post(
            f"/api/tasks/{self.task.pk}/attachments/",
            {"file": test_file},
            format="multipart",
        )
        self.assertEqual(TaskAttachment.objects.count(), 1)
        attachment = TaskAttachment.objects.first()
        self.assertEqual(attachment.task, self.task)
        self.assertEqual(attachment.uploaded_by, self.user)

    def test_list_attachments(self):
        """Should list all attachments for a task."""
        # Upload two files
        for name in ["file1.txt", "file2.txt"]:
            self.client.post(
                f"/api/tasks/{self.task.pk}/attachments/",
                {"file": self._create_test_file(name=name)},
                format="multipart",
            )

        response = self.client.get(
            f"/api/tasks/{self.task.pk}/attachments/"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 2)

    def test_upload_rejects_oversized_file(self):
        """Should reject files larger than MAX_FILE_SIZE_MB."""
        # Create a file that's > 10MB
        original_max = TaskAttachment.MAX_FILE_SIZE_MB
        TaskAttachment.MAX_FILE_SIZE_MB = 0  # 0 MB limit for testing
        try:
            test_file = self._create_test_file(content=b"x" * 100)
            response = self.client.post(
                f"/api/tasks/{self.task.pk}/attachments/",
                {"file": test_file},
                format="multipart",
            )
            self.assertEqual(response.status_code, 400)
        finally:
            TaskAttachment.MAX_FILE_SIZE_MB = original_max

    def test_upload_rejects_invalid_extension(self):
        """Should reject files with disallowed extensions."""
        test_file = self._create_test_file(
            name="malware.exe", content=b"evil"
        )
        response = self.client.post(
            f"/api/tasks/{self.task.pk}/attachments/",
            {"file": test_file},
            format="multipart",
        )
        self.assertEqual(response.status_code, 400)

    def test_delete_attachment(self):
        """Owner should be able to delete their attachment."""
        test_file = self._create_test_file()
        upload_response = self.client.post(
            f"/api/tasks/{self.task.pk}/attachments/",
            {"file": test_file},
            format="multipart",
        )
        attachment_id = upload_response.data["id"]

        response = self.client.delete(f"/api/attachments/{attachment_id}/")
        self.assertEqual(response.status_code, 204)
        self.assertEqual(TaskAttachment.objects.count(), 0)

    def test_delete_attachment_forbidden_for_non_owner(self):
        """Non-owner should not be able to delete an attachment."""
        test_file = self._create_test_file()
        upload_response = self.client.post(
            f"/api/tasks/{self.task.pk}/attachments/",
            {"file": test_file},
            format="multipart",
        )
        attachment_id = upload_response.data["id"]

        # Switch to another user
        other_user = User.objects.create_user(
            username="other", password="pass"
        )
        other_token = Token.objects.create(user=other_user)
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Token {other_token.key}"
        )

        response = self.client.delete(f"/api/attachments/{attachment_id}/")
        self.assertEqual(response.status_code, 403)

    def test_download_attachment(self):
        """Should be able to download the uploaded file."""
        test_file = self._create_test_file(content=b"Download me!")
        upload_response = self.client.post(
            f"/api/tasks/{self.task.pk}/attachments/",
            {"file": test_file},
            format="multipart",
        )
        attachment_id = upload_response.data["id"]

        response = self.client.get(
            f"/api/attachments/{attachment_id}/download/"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response["Content-Disposition"],
            'attachment; filename="test.txt"',
        )

    def test_upload_to_nonexistent_task(self):
        """Should return 404 for uploading to a non-existent task."""
        test_file = self._create_test_file()
        response = self.client.post(
            "/api/tasks/99999/attachments/",
            {"file": test_file},
            format="multipart",
        )
        self.assertEqual(response.status_code, 404)

    def test_upload_image_thumbnail(self):
        """Should accept image files as thumbnails."""
        # Create a minimal valid PNG (1x1 pixel)
        import struct
        import zlib

        def _create_png():
            # IHDR
            width = 1
            height = 1
            bit_depth = 8
            color_type = 2  # RGB
            ihdr_data = struct.pack(">IIBBBBB", width, height, bit_depth, color_type, 0, 0, 0)
            ihdr_crc = zlib.crc32(b"IHDR" + ihdr_data)
            ihdr = struct.pack(">I", 13) + b"IHDR" + ihdr_data + struct.pack(">I", ihdr_crc & 0xFFFFFFFF)

            # IDAT
            raw_data = b"\x00\xff\x00\x00"  # filter byte + RGB pixel
            compressed = zlib.compress(raw_data)
            idat_crc = zlib.crc32(b"IDAT" + compressed)
            idat = struct.pack(">I", len(compressed)) + b"IDAT" + compressed + struct.pack(">I", idat_crc & 0xFFFFFFFF)

            # IEND
            iend_crc = zlib.crc32(b"IEND")
            iend = struct.pack(">I", 0) + b"IEND" + struct.pack(">I", iend_crc & 0xFFFFFFFF)

            return b"\x89PNG\r\n\x1a\n" + ihdr + idat + iend

        png_data = _create_png()
        thumbnail = SimpleUploadedFile(
            "thumb.png", png_data, content_type="image/png"
        )
        test_file = self._create_test_file()

        response = self.client.post(
            f"/api/tasks/{self.task.pk}/attachments/",
            {"file": test_file, "thumbnail": thumbnail},
            format="multipart",
        )
        self.assertEqual(response.status_code, 201)


# ===========================================================================
# 7. TASK CRUD INTEGRATION TESTS
# ===========================================================================

class TaskCRUDTest(APITestCase):
    """Integration tests for task CRUD with all concepts working together."""

    def setUp(self):
        self.user = User.objects.create_user(
            username="cruduser", password="testpass123"
        )
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Token {self.token.key}"
        )
        cache.clear()

    def test_create_task(self):
        """POST /api/tasks/ should create a task and fire signals."""
        response = self.client.post(
            "/api/tasks/",
            {"title": "Test Task", "description": "A test task"},
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["title"], "Test Task")
        self.assertEqual(response.data["owner"], "cruduser")
        self.assertEqual(response.data["status"], "todo")

    def test_list_tasks(self):
        """GET /api/tasks/ should list all tasks."""
        Task.objects.create(title="Task 1", owner=self.user)
        Task.objects.create(title="Task 2", owner=self.user)

        response = self.client.get("/api/tasks/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 2)

    def test_get_task_detail(self):
        """GET /api/tasks/<pk>/ should return task details."""
        task = Task.objects.create(
            title="Detail Task", owner=self.user
        )
        response = self.client.get(f"/api/tasks/{task.pk}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], "Detail Task")

    def test_update_task(self):
        """PUT /api/tasks/<pk>/ should update the task."""
        task = Task.objects.create(
            title="Original", owner=self.user
        )
        response = self.client.put(
            f"/api/tasks/{task.pk}/",
            {"title": "Updated", "status": "done"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], "Updated")
        self.assertEqual(response.data["status"], "done")

    def test_update_task_forbidden_for_non_owner(self):
        """Non-owner should not be able to update a task."""
        task = Task.objects.create(title="Protected", owner=self.user)

        other_user = User.objects.create_user(
            username="other", password="pass"
        )
        other_token = Token.objects.create(user=other_user)
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Token {other_token.key}"
        )

        response = self.client.put(
            f"/api/tasks/{task.pk}/", {"title": "Hacked"}
        )
        self.assertEqual(response.status_code, 403)

    def test_delete_task(self):
        """DELETE /api/tasks/<pk>/ should delete the task."""
        task = Task.objects.create(title="Delete Me", owner=self.user)
        response = self.client.delete(f"/api/tasks/{task.pk}/")
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Task.objects.count(), 0)

    def test_attachment_count_in_serializer(self):
        """Task serializer should include attachment count."""
        task = Task.objects.create(title="With Files", owner=self.user)
        # Create attachment without actual file for quick test
        TaskAttachment.objects.create(
            task=task,
            original_filename="test.txt",
            file_size=100,
            uploaded_by=self.user,
        )

        response = self.client.get(f"/api/tasks/{task.pk}/")
        self.assertEqual(response.data["attachment_count"], 1)

    def test_full_workflow(self):
        """
        End-to-end test: create task → update status → verify signals.
        Tests that middleware, signals, and caching all work together.
        """
        # Create
        create_response = self.client.post(
            "/api/tasks/",
            {"title": "Full Workflow Test"},
        )
        task_id = create_response.data["id"]

        # Read (should cache)
        self.client.get(f"/api/tasks/{task_id}/")

        # Update status (triggers custom signal + cache invalidation)
        self.client.put(
            f"/api/tasks/{task_id}/",
            {"status": "in_progress"},
        )

        # Verify cache was invalidated
        self.assertIsNone(cache.get(f"task_detail_{task_id}"))

        # Read again (fresh from DB)
        response = self.client.get(f"/api/tasks/{task_id}/")
        self.assertEqual(response.data["status"], "in_progress")

        # Delete
        self.client.delete(f"/api/tasks/{task_id}/")
        self.assertEqual(Task.objects.count(), 0)


# ===========================================================================
# 8. QUERY OPTIMIZATION TESTS
# ===========================================================================

class TaskQueryOptimizationTest(TestCase):
    """Demonstrate N+1 queries and Django's relationship loading helpers."""

    def setUp(self):
        for index in range(3):
            owner = User.objects.create_user(username=f"queryuser{index}")
            task = Task.objects.create(
                title=f"Query Task {index}",
                owner=owner,
            )
            TaskAttachment.objects.create(
                task=task,
                original_filename=f"attachment{index}.txt",
                file_size=100,
                uploaded_by=owner,
            )

    def test_traditional_task_retrieval_causes_n_plus_one_queries(self):
        """Loading each task owner separately adds one query per task."""
        with self.assertNumQueries(4):
            tasks = list(Task.objects.all())
            owners = [task.owner.username for task in tasks]

        self.assertEqual(owners, ["queryuser0", "queryuser1", "queryuser2"])

    def test_select_related_loads_task_owners_in_one_query(self):
        """select_related joins each task's owner into the task query."""
        with self.assertNumQueries(1):
            tasks = list(Task.objects.select_related("owner"))
            owners = [task.owner.username for task in tasks]

        self.assertEqual(owners, ["queryuser0", "queryuser1", "queryuser2"])

    def test_prefetch_related_loads_task_attachments_in_two_queries(self):
        """prefetch_related fetches tasks and their attachments separately."""
        with self.assertNumQueries(2):
            tasks = list(Task.objects.prefetch_related("attachments"))
            attachment_names = [
                attachment.original_filename
                for task in tasks
                for attachment in task.attachments.all()
            ]

        self.assertEqual(
            attachment_names,
            ["attachment0.txt", "attachment1.txt", "attachment2.txt"],
        )
