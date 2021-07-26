from django.urls import path 
from give_print import views

appname = "give_print"

urlpatterns = [
    path("", views.home, name = 'home'),
]
