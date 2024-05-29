from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    '''
    Profile model for each user
    '''
       
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pic.jpg',upload_to='profile_pics')
    location = models.CharField(max_length=400)
    
    # String representation should return username of that user
    def __str__(self):
        
        return self.user.username
    