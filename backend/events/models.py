import random
from django.db import models
from django.conf import settings
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth.models import User


def generate_pin():
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=6))

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    date = models.DateTimeField()
    code = models.CharField(max_length=6, default=generate_pin, unique=True)
    theme = models.CharField(max_length=255, blank=True, null=True)
    host = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.date + timedelta(days=2) < timezone.now():
            self.is_active = False
        super().save(*args, **kwargs)

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

class SongRequest(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='song_requests')
    song = models.ForeignKey('songs.Song', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)
    
    def upvote(self):
        self.votes += 1
        self.save()
        return self
