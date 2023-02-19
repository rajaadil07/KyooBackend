from accounts.models import Host
from music_api.models import Song

from django.db import models
from django.core.validators import RegexValidator

import random
import string

def generate_event_code():
    length = 6
    while True:
        code = ''.join(random.choices(string.ascii_uppercase,k=length))
        if Event.objects.filter(pin_code=code).count() == 0:
            break
    return code

class Event(models.Model):
    name = models.CharField(max_length=255)
    host = models.ForeignKey(Host, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField()
    queue = models.ManyToManyField(Song)
    pin_code = models.CharField(max_length=8, default="", unique=True)
    qr_code = models.CharField(max_length=50, unique=True, validators=[RegexValidator(regex=r'^[0-9A-Fa-f]+$')])

    def __str__(self):
        return self.name