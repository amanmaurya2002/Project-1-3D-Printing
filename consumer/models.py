from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# table for user data
class Consumer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    part = models.FileField(upload_to="uploaded_parts", blank=True)