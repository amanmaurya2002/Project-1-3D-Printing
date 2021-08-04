from django.contrib import admin
from .models import *

class PrinterAdmin(admin.ModelAdmin):
    list_display = ("id", "make", "model", "process")

# Register your models here.
admin.site.register(Supplier)
admin.site.register(Printer, PrinterAdmin)
admin.site.register(Process)
admin.site.register(Material)
admin.site.register(Colour)