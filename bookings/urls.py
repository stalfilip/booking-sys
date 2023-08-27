from django.urls import path
from . import views
from . import views

urlpatterns = [

    path('add-resource/', views.add_resource, name='add_resource'),
    path('resources/', views.all_resources, name='all_resources'),
    path('login/', views.custom_login, name='custom_login'),
    path('logout/', views.custom_logout, name='logga_ut'),
    path('customers/', views.users_view, name='users_view'),

]
