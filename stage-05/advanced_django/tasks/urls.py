from django.urls import path
from .views import (
    CurrentUserView,
    OAuthTaskListView,
    TaskListCreateView,
    TaskDetailView,
    TaskAttachmentListView,
    TaskAttachmentDetailView,
    AttachmentDownloadView,
    CacheDemoView,
    ThrottleDemoView,
)
from .views import async_demo

urlpatterns = [
    # Auth demo
    path("me/", CurrentUserView.as_view(), name="current_user"),

    # OAuth2-only endpoint
    path("oauth/tasks/", OAuthTaskListView.as_view(), name="oauth_task_list"),

    # Task CRUD (signals fire on save/delete, caching on GET)
    path("tasks/", TaskListCreateView.as_view(), name="task_list_create"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task_detail"),

    # File upload & management
    path(
        "tasks/<int:task_id>/attachments/",
        TaskAttachmentListView.as_view(),
        name="task_attachments",
    ),
    path(
        "attachments/<int:pk>/",
        TaskAttachmentDetailView.as_view(),
        name="attachment_detail",
    ),
    path(
        "attachments/<int:pk>/download/",
        AttachmentDownloadView.as_view(),
        name="attachment_download",
    ),

    # Caching demo
    path("cache-demo/", CacheDemoView.as_view(), name="cache_demo"),

    # Async demo
    path("async-demo/", async_demo, name="async_demo"),

    # Throttling demo
    path(
    "throttle-demo/",
    ThrottleDemoView.as_view(),
    name="throttle_demo",
),
]