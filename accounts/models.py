from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

from datetime import date

class Host(AbstractUser):
    display_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True)
    birthdate = models.DateField(blank=True, null=True)
    groups = models.ManyToManyField(
        Group, related_name='hosts', blank=True, help_text='The groups this host belongs to. A host will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission, related_name='hosts', blank=True, help_text='Specific permissions for this host.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return f"{self.display_name}"

    def age(self):
        today = date.today()
        age = today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
        return age