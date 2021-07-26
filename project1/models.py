from django.db import models
from get_print.models import Customer, Part
from give_print.models import Supplier, Technology, Material, Colour
from django.core.validators import MaxValueValidator

class PrintSpecification(models.Model):
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE, blank=True)
    material = models.ForeignKey(Material, on_delete=models.CASCADE, blank=True)
    colour = models.ForeignKey(Colour, on_delete=models.CASCADE, blank=True)
    infill = models.PositiveSmallIntegerField(validators=[MaxValueValidator(100)])

class Order(models.Model):
    buyer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    seller = models.ForeignKey(Supplier, on_delete=models.PROTECT)
    specification = models.ForeignKey(PrintSpecification, on_delete=models.PROTECT)
    part = models.ForeignKey(Part, on_delete=models.PROTECT)