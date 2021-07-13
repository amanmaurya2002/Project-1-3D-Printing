from django.contrib import admin
from home.models import Newuser

# Register your models here.
from home.models import Contact
admin.site.register(Contact)
admin.site.register(Newuser)