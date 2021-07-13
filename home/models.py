from datetime import date
from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=123)
    phone = models.CharField(max_length=15)
    desc = models.TextField()
    date = models.DateField()

class Newuser(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=130)
    Pwd = models.CharField(max_length=15)
    
    

    


