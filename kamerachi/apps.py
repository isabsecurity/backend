from django.apps import AppConfig


class KamerachiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'kamerachi'
    def ready(self):
        import kamerachi.signals