from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Process(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Material(models.Model):
    name = models.CharField(max_length=100)
    processes = models.ManyToManyField(Process)

    def __str__(self):
        return self.name

class Colour(models.Model):
    name = models.CharField(max_length=50)
    materials = models.ManyToManyField(Material)
    
    def __str__(self):
        return self.name

class Printer(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    process = models.ForeignKey(Process, on_delete=models.CASCADE, related_name='printers')
    build_volume = models.ForeignKey

    def __str__(self):
        return f"{self.make} {self.model}"

class Supplier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    printers = models.ManyToManyField(Printer, related_name='with_suppliers')
    materials = models.ManyToManyField(Material, related_name='with_suppliers')

    def __str__(self):
        return self.user.username