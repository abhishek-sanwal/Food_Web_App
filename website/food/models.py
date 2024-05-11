from django.db import models

# Create your models here.

'''
Creating a model for each food item, ID will be auto-assigned by django-ORM
after each item is saved in db.
'''
class Item(models.Model):
    
    item_name = models.CharField(max_length=100)
    item_description = models.CharField(max_length=200)
    item_price = models.IntegerField(default = 100)
    item_image = models.CharField(max_length=300,default="https://www.food4fuel.com/wp-content/uploads/woocommerce-placeholder-600x600.png")
    
    def __str__(self):
        
        return self.item_name
