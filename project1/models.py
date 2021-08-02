from django.db import models
from django.db.models.deletion import PROTECT
from get_print.models import Customer, Part
from give_print.models import Supplier, Process, Material, Colour
from django.contrib.auth.models import User

class Unit(models.Model):
    unit = models.CharField(max_length=10)

    def __str__(self):
        return self.unit

class Resolution(models.Model):
    resolution = models.CharField(max_length=50)

    def __str__(self):
        return self.resolution

class PrintSpecification(models.Model):
    part = models.FileField(upload_to='uploads/instant_quote')
    units = models.ForeignKey(Unit, on_delete=models.PROTECT)
    resolution = models.ForeignKey(Resolution, on_delete=models.PROTECT)
    process = models.ForeignKey(Process, on_delete=models.PROTECT, blank=True)
    material = models.ForeignKey(Material, on_delete=models.PROTECT, blank=True)
    colour = models.ForeignKey(Colour, on_delete=models.PROTECT, blank=True)
    additional_info = models.TextField()
    copies = models.PositiveIntegerField()
    buyer = models.ForeignKey(User, on_delete=PROTECT)

class ShippingInfo(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=500)
    pin_code = models.PositiveSmallIntegerField()
    city = models.CharField(max_length=100)
    buyer = models.ForeignKey(User, on_delete=PROTECT)

class Order(models.Model):
    buyer = models.ForeignKey(User, on_delete=PROTECT)
    seller = models.ForeignKey(Supplier, on_delete=models.PROTECT)
    specification = models.ForeignKey(PrintSpecification, on_delete=models.PROTECT)
    shipping_info = models.ForeignKey(ShippingInfo, on_delete=models.PROTECT)
