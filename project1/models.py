from get_print.views import part
from django.db import models
from get_print.models import Customer, Part
from give_print.models import Supplier, Process, Material, Colour
from django.core.validators import MaxValueValidator

class Unit(models.Model):
    unit = models.CharField()

class PrintSpecification(models.Model):
    part = models.ForeignKey(Part, on_delete=models.PROTECT)
    units = models.ForeignKey(Unit, on_delete=models.PROTECT)
    process = models.ForeignKey(Process, on_delete=models.CASCADE, blank=True)
    material = models.ForeignKey(Material, on_delete=models.CASCADE, blank=True)
    colour = models.ForeignKey(Colour, on_delete=models.CASCADE, blank=True)
    infill = models.PositiveSmallIntegerField(validators=[MaxValueValidator(100)])

class Order(models.Model):
    buyer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    seller = models.ForeignKey(Supplier, on_delete=models.PROTECT)
    specification = models.ForeignKey(PrintSpecification, on_delete=models.PROTECT)
