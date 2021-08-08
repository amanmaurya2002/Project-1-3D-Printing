from django.contrib import admin
from django.urls import path 
from get_print import views

app_name = 'get_print'

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('register', views.register_request, name='register'),
    path('login', views.login_request, name='login'),
    path('logout', views.logout_request, name='logout'),
    path('workspace', views.workspace, name='workspace'),
    path('parts', views.parts, name='parts'),
    path('parts/<int:part_id>', views.part, name='part'),
    path('upload_part', views.upload_part, name='upload_part'),
    path('orders', views.orders, name='orders'),
    path('quotes', views.quotes, name='quotes'),
    path('order-status', views.order_status, name='order_status'),
    path('projects', views.projects, name='projects'),
    path('materials', views.materials, name='materials'),
    path('technologies', views.technologies, name='technologies'),
]
