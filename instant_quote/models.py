from django.db import models

# Create your models here.

# table for all parts
class Part(models.Model):
    part = models.FileField(upload_to='uploads')

    def __str__(self):
        return self.part.name
