from django.urls import path 
from instant_quote import views

app_name = 'instant_quote'

urlpatterns = [
    path('', views.index, name = 'index'),
]
