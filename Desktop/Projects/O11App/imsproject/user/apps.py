from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'

    #This is for profile enforcement
    def ready(self):
        from user import signals
