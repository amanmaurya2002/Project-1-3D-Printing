from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Colour(models.Model):
    colour = models.TextField(max_length=50)
    
    def __str__(self):
        return self.colour

class Material(models.Model):
    name = models.TextField(max_length=100)
    colours = models.ManyToManyField(Colour, related_name='materials')

    def __str__(self):
        return self.name

class Technology(models.Model):
    name = models.TextField(max_length=100)
    materials = models.ManyToManyField(Material, related_name='printing_technologies')

    def __str__(self):
        return self.name

class Printer(models.Model):
    make = models.TextField(max_length=100)
    model = models.TextField(max_length=100)
    printing_technology = models.ForeignKey(Technology, on_delete=models.CASCADE, related_name='printers')

    def __str__(self):
        return f"{self.make} {self.model}"

class Supplier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    printers = models.ManyToManyField(Printer, related_name='with_suppliers')
    materials = models.ManyToManyField(Material, related_name='with_suppliers')

    def __str__(self):
        return self.user.username