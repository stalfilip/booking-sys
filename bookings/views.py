from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import ResourceForm
from .models import Resource
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

def homepage(request):
    return render(request, 'homepage.html')

def users_view(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})

@login_required
def add_resource(request):
    if not request.user.is_staff:
        return HttpResponseForbidden("Endast administratörer får lägga till resurser.")
    
    # Om användaren är inloggad och är staff
    if request.method == "POST":
        form = ResourceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/')  #Skickar tillbaks till hemskärmen
    else:
        form = ResourceForm()

    return render(request, 'add_resource.html', {'form': form})

def all_resources(request):
    resources = Resource.objects.all()
    return render(request, 'resources_list.html', {'resources': resources})

def custom_login(request):
    error_message = None

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('homepage')
        else:
            error_message = "Felaktiga inloggningsuppgifter eller behörighet saknas."

    return render(request, 'login.html', {'error_message': error_message})

def custom_logout(request):
    logout(request)
    return redirect('homepage')
