from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.

def say_hello(request):
    return render(request,'hello.html')

def homepage(request):
    return render(request, 'homepage.html')

from django.shortcuts import render
from .models import Customer

def users_view(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})
