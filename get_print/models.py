from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

# table for all parts
class Part(models.Model):
    part = models.FileField(upload_to='uploads')

    def __str__(self):
        return self.part.name

# table for user data
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    parts = models.ManyToManyField(Part, blank=True, related_name='uploaded_by')

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_customer(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)
    else:
        instance.customer.save()
