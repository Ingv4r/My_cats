from django.apps import AppConfig


class CatsConfig(AppConfig):
    """Config for cats app."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cats'
