from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class Customer(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)
    address = models.TextField(blank=True, null=True)

    # Add related_name to avoid conflicts
    groups = models.ManyToManyField(Group, related_name="customer_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="customer_permissions", blank=True)

    def __str__(self):
        return self.username
