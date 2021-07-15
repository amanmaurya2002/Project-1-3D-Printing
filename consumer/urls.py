from django.contrib import admin
from django.urls import path 
from consumer import views

urlpatterns = [
    path("", views.home, name = 'home'),
    path("about", views.about, name = 'about'),
    path("register", views.register, name = 'register'),
    path("login", views.login, name = 'login'),
    
]
