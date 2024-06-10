from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    # For activating django signals. It is necessary to include
    # below code
    def ready(self) -> None:
        import users.signals
        return super().ready()
