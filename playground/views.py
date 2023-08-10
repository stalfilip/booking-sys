from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def say_hello(request):
    return render(request,'hello.html')

def homepage(request):
    return render(request, 'homepage.html')

from django.shortcuts import render
from .models import Customer

def customers_view(request):
    customers = Customer.objects.all()
    return render(request, 'customers.html', {'customers': customers})
