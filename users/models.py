from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class CustomUser(AbstractUser):
    USER_TYPES = (
        ('author', 'Author'),
        ('client', 'Client'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='client')
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Add this line to avoid conflicts
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  # Add this line to avoid conflicts
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    REQUIRED_FIELDS = []
