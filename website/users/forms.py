
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models


class RegisterForm(UserCreationForm):
    
    email = models.EmailField()
    
    class Meta:
        
        model = User
        fields = ['username','email','password1','password2']        
        