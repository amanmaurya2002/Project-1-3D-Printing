from django.contrib import admin
from django.urls import path 
from consumer import views

urlpatterns = [
    path("", views.home, name = 'home'),
    path("about", views.about, name = 'about'),
    path("register", views.register_request, name = 'register'),
    path("login", views.login_request, name = 'login'),
    path("logout", views.logout_request, name = 'logout'),
    path("print", views.print, name = 'print'),
]
