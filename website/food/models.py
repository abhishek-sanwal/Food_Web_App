from django.db import models
from django.contrib.auth.models import User
# Create your models here.

'''
Creating a model for each food item, ID will be auto-assigned by django-ORM
after each item is saved in db.
'''
from django.urls import reverse


# Item has 1:1 mapping with Auth.user.
class Item(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    item_description = models.CharField(max_length=200)
    item_price = models.IntegerField(default=100)
    item_image = models.CharField(max_length=300,
                                  default="https://www.food4fuel.com/wp-content\
                /uploads/woocommerce-placeholder-600x600.png")

    def __str__(self) -> str:

        return self.item_name

    # Whenenver an item is created it will redirect to that
    # Particular item deatil page

    def get_absolute_url(self):

        return reverse("food:display", kwargs={"item_id": self.pk})
