from rest_framework import serializers
from .models import Task, TaskAttachment


class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(
        source="owner.username",
        read_only=True,
    )
    attachment_count = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "status",
            "owner",
            "attachment_count",
            "created_at",
            "updated_at",
        ]

    def get_attachment_count(self, obj):
        return obj.attachments.count()


class TaskCreateSerializer(serializers.ModelSerializer):
    """
    Separate serializer for creating tasks.
    owner is set automatically from the request user.
    """

    class Meta:
        model = Task
        fields = ["id", "title", "description", "status"]
        read_only_fields = ["id"]


class TaskAttachmentSerializer(serializers.ModelSerializer):
    """
    File Upload serializer.

    Learning Points:
    - FileField in serializer handles multipart form data
    - We auto-populate original_filename, file_size, content_type from the upload
    - uploaded_by is set from request.user in the view
    """

    file_size_display = serializers.ReadOnlyField()
    uploaded_by = serializers.CharField(
        source="uploaded_by.username",
        read_only=True,
    )

    class Meta:
        model = TaskAttachment
        fields = [
            "id",
            "task",
            "file",
            "thumbnail",
            "original_filename",
            "file_size",
            "file_size_display",
            "content_type",
            "uploaded_by",
            "uploaded_at",
        ]
        read_only_fields = [
            "id",
            "original_filename",
            "file_size",
            "content_type",
            "uploaded_by",
            "uploaded_at",
        ]


class TaskAttachmentUploadSerializer(serializers.Serializer):
    """
    Minimal serializer just for the upload endpoint.
    Validates only the file input; other fields are auto-populated.
    """

    file = serializers.FileField()
    thumbnail = serializers.ImageField(required=False)

    def validate_file(self, value):
        """Validate file size and type."""
        import os

        max_size = TaskAttachment.MAX_FILE_SIZE_MB * 1024 * 1024
        if value.size > max_size:
            raise serializers.ValidationError(
                f"File too large. Max size: {TaskAttachment.MAX_FILE_SIZE_MB}MB"
            )

        ext = os.path.splitext(value.name)[1].lower()
        if ext not in TaskAttachment.ALLOWED_EXTENSIONS:
            raise serializers.ValidationError(
                f"Unsupported file type '{ext}'. "
                f"Allowed: {', '.join(sorted(TaskAttachment.ALLOWED_EXTENSIONS))}"
            )

        return value