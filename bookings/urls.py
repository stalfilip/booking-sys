from django.urls import path
from . import views

urlpatterns = [
    path('add-resource/', views.add_resource, name='add_resource'),
]
