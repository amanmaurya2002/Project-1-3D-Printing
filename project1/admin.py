from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(PrintSpecification)
admin.site.register(Order)
admin.site.register(ShippingInfo)
admin.site.register(Unit)
admin.site.register(Resolution)