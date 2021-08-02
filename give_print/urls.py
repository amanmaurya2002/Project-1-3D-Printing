from django.urls import path 
from give_print import views

app_name = "give_print"

urlpatterns = [
    path("", views.home, name = 'home'),
    path("about", views.about, name = 'about'),
    path("register", views.register_request, name = 'register'),
    path("login", views.login_request, name = 'login'),
    path("logout", views.logout_request, name = 'logout'),
    path("dashboard", views.dashboard, name = 'dashboard'),
]
