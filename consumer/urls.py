from django.contrib import admin
from django.urls import path 
from consumer import views

urlpatterns = [
    path("", views.home, name = 'consumer'),
    path("about", views.about, name = 'about'),
    path("register", views.register, name = 'register'),
    path("contact", views.contact, name = 'supplier'),
    path("login", views.login, name = 'login'),
    
]
