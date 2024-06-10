from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
# Create your views here.
from .forms import RegisterForm
from django.http import HttpResponse


def register(request):

    user = RegisterForm(request.POST or None)
    if request.method == "POST" and user.is_valid():
        user.save()
        username = user.cleaned_data.get('username')
        messages.success(request, f"Welcome {username} to our Website.")
        return redirect('login')
    return render(request, 'register_user.html', {
        'form': user
    })


@login_required
def profile(request):

    return render(request, 'profle.html')


def hello(request):
    return HttpResponse("<h1> Welcome to our website.Add food in url. </h1>")
