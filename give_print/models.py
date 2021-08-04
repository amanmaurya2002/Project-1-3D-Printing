from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Colour(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.colour

class Material(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.material

class Process(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.process

class Printer(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    process = models.ForeignKey(Process, on_delete=models.CASCADE, related_name='printers')
    supported_materials = models.ManyToManyField(Material)


    def __str__(self):
        return f"{self.make} {self.model}"

class Supplier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    printers = models.ManyToManyField(Printer, related_name='with_suppliers')
    materials = models.ManyToManyField(Material, related_name='with_suppliers')

    def __str__(self):
        return self.user.username