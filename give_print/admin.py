from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Supplier)
admin.site.register(Printer)
admin.site.register(Process)
admin.site.register(Material)
admin.site.register(Colour)