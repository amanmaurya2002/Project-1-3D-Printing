from django.contrib import admin
from consumer.models import Newuser

# Register your models here.
from consumer.models import Contact
admin.site.register(Contact)
admin.site.register(Newuser)