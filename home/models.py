from django.db import models

# Create your models here.

# Table for supplier information.
class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=123)
    phone = models.CharField(max_length=15)
    date = models.DateField()

# Table for user credentials.
class Newuser(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=130)
    Pwd = models.CharField(max_length=15)
    
    

    


