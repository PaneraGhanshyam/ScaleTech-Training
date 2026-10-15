from django.conf import settings
from django.db import models


class Task(models.Model):
    STATUS_CHOICES = [
        ("todo", "To do"),
        ("in_progress", "In progress"),
        ("done", "Done"),
    ]

    title = models.CharField(max_length=200,db_index=True)
    description = models.TextField(blank=True)

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tasks",
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="todo",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class TaskAttachment(models.Model):
    """
    File Upload & Management
    ========================
    Demonstrates Django's file handling with ImageField and FileField.

    Learning Points:
    1. FileField — stores any file (PDF, doc, zip, etc.)
    2. ImageField — inherits from FileField, adds image validation (needs Pillow)
    3. upload_to — controls the subdirectory structure in MEDIA_ROOT
    4. File size/type validation in clean()
    5. django-cleanup auto-deletes files when model instances are deleted
    """

    ALLOWED_EXTENSIONS = {
        ".jpg", ".jpeg", ".png", ".gif", ".webp",  # Images
        ".pdf", ".doc", ".docx", ".txt",            # Documents
        ".zip", ".tar", ".gz",                       # Archives
    }
    MAX_FILE_SIZE_MB = 10

    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name="attachments",
    )

    file = models.FileField(
        upload_to="attachments/%Y/%m/%d/",
        help_text="Upload any file (max 10MB)",
    )

    # Optional: separate image field with automatic validation
    thumbnail = models.ImageField(
        upload_to="thumbnails/%Y/%m/%d/",
        blank=True,
        null=True,
        help_text="Optional image thumbnail (auto-validated by Pillow)",
    )

    original_filename = models.CharField(max_length=255)
    file_size = models.PositiveIntegerField(help_text="File size in bytes")
    content_type = models.CharField(max_length=100, blank=True)
    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="uploaded_attachments",
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-uploaded_at"]

    def __str__(self):
        return f"{self.original_filename} (Task: {self.task.title})"

    @property
    def file_size_display(self):
        """Human-readable file size."""
        size = self.file_size
        for unit in ["B", "KB", "MB", "GB"]:
            if size < 1024:
                return f"{size:.1f} {unit}"
            size /= 1024
        return f"{size:.1f} TB"

    def clean(self):
        """Validate file size and extension."""
        from django.core.exceptions import ValidationError
        import os

        if self.file:
            # Validate file size
            if self.file.size > self.MAX_FILE_SIZE_MB * 1024 * 1024:
                raise ValidationError(
                    f"File too large. Maximum size is {self.MAX_FILE_SIZE_MB}MB."
                )

            # Validate file extension
            ext = os.path.splitext(self.file.name)[1].lower()
            if ext not in self.ALLOWED_EXTENSIONS:
                raise ValidationError(
                    f"Unsupported file type '{ext}'. "
                    f"Allowed: {', '.join(sorted(self.ALLOWED_EXTENSIONS))}"
                )