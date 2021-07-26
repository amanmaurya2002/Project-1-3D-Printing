from django.db import models
from get_print.models import Customer, Part
from give_print.models import Supplier, Technology, Material, Colour

class PrintSpecification(models.Model):
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    colour = models.ForeignKey(Colour, on_delete=models.CASCADE)
    infill = models.PositiveSmallIntegerField()

class Order(models.Model):
    buyer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    seller = models.ForeignKey(Supplier, on_delete=models.PROTECT)
    specification = models.ForeignKey(PrintSpecification, on_delete=models.PROTECT)
    part = models.ForeignKey(Part, on_delete=models.PROTECT)