from django.db import models
from django.db.models.deletion import PROTECT
from get_print.models import Customer, Part
from give_print.models import Supplier, Process, Material, Colour
from django.contrib.auth.models import User
from smart_selects.db_fields import ChainedForeignKey, ChainedManyToManyField

class Unit(models.Model):
    unit = models.CharField(max_length=10)

    def __str__(self):
        return self.unit

class Resolution(models.Model):
    resolution = models.CharField(max_length=50)

    def __str__(self):
        return self.resolution

class PrintSpecification(models.Model):
    units = models.ForeignKey(Unit, on_delete=models.PROTECT)
    resolution = models.ForeignKey(Resolution, on_delete=models.PROTECT)
    process = models.ForeignKey(Process, on_delete=models.PROTECT, blank=True)
    material = ChainedForeignKey(
        Material,
        chained_field='process',
        chained_model_field='processes')
    colours = ChainedManyToManyField(
        Colour,
        horizontal=True,
        chained_field='material',
        chained_model_field='materials')
    additional_info = models.TextField(blank=True)
    copies = models.PositiveIntegerField(default=1)

class ShippingInfo(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=500)
    pin_code = models.PositiveSmallIntegerField()
    city = models.CharField(max_length=100)

class Order(models.Model):
    buyer = models.ForeignKey(User, on_delete=PROTECT)
    seller = models.ForeignKey(Supplier, on_delete=models.PROTECT)
    part = models.ForeignKey(Part, on_delete=PROTECT)
    specification = models.ForeignKey(PrintSpecification, on_delete=models.PROTECT)
    shipping_info = models.ForeignKey(ShippingInfo, on_delete=models.PROTECT)
    fulfilled = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)
