import random
from django.db import models
from django.conf import settings

def generate_pin():
    return ''.join(random.choices('0123456789', k=6))

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    date = models.DateTimeField()
    code = models.CharField(max_length=6, default=generate_pin, unique=True)
    qr_code = models.ImageField(upload_to='events/qr_codes/', blank=True, null=True)
    theme = models.CharField(max_length=255, blank=True, null=True)
    host = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='hosted_events')
    is_active = models.BooleanField(default=True)

class EventUser(models.Model):
    ROLES = (
        ('attendee', 'Attendee'),
        ('dj', 'DJ'),
        ('host', 'Host'),
    )
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='participants')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='joined_events')
    role = models.CharField(max_length=20, choices=ROLES, default='attendee')
    joined_at = models.DateTimeField(auto_now_add=True)
