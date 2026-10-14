from django.apps import AppConfig


class TasksConfig(AppConfig):
    name = 'tasks'

    def ready(self):
        """
        Import signals when the app is ready.

        WHY HERE?
        - Signal receivers must be imported AFTER the app registry is populated
        - AppConfig.ready() is the official hook for this
        - If you import signals at module level, you risk circular imports
        """
        import tasks.signals  # noqa: F401
