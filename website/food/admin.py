from django.contrib import admin
from . import models
# Register your models here.

'''
If you want to see models in admin.panel then registering them in admin.py
is must. for each model
'''
admin.site.register(models.Item)