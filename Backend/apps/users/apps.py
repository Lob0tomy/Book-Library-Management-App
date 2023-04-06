from django.apps import AppConfig
from library_management.settings import AUTH_USER_MODEL


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.users'