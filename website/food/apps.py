from django.apps import AppConfig

# Configuration for app We can include this in
# settings.py of project or directly add appname
class FoodConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'food'
