from django.contrib import admin
from .models import Task, TaskAttachment


class TaskAttachmentInline(admin.TabularInline):
    model = TaskAttachment
    extra = 0
    readonly_fields = ("original_filename", "file_size", "content_type", "uploaded_by", "uploaded_at")


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("title", "description")
    inlines = [TaskAttachmentInline]


@admin.register(TaskAttachment)
class TaskAttachmentAdmin(admin.ModelAdmin):
    list_display = ("original_filename", "task", "file_size", "uploaded_by", "uploaded_at")
    list_filter = ("uploaded_at",)
    readonly_fields = ("original_filename", "file_size", "content_type")
