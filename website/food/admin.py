from django.contrib import admin
from . import models
# Register your models here.

'''
If you want to see models in admin.panel then registering them in admin.py
is must. for each model
'''
# To show this model in Admin console it must be register here
admin.site.register(models.Item)