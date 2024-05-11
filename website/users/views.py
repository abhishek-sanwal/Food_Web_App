from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render,redirect
# Create your views here.
from .forms import RegisterForm

def register(request):
    
    user = RegisterForm(request.POST or None)
    if request.method == "POST" and user.is_valid():
            user.save()
            username = user.cleaned_data.get('username')
            messages.success(request, f"Welcome {username} to our Website.")
            return redirect('login')
    return render(request,'register_user.html',{
        'form' : user
    })        
