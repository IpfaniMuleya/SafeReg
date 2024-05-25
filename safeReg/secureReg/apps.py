from django.apps import AppConfig


class SecureregConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'secureReg'

    def ready(self):
        import secureReg.signals