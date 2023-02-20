from accounts.models import Host
from music_api.models import Song

from django.db import models
from datetime import date

import base64
import io
import qrcode
import random
import string

def generate_event_code():
    length = 6
    while True:
        code = ''.join(random.choices(string.ascii_uppercase,k=length))
        if Event.objects.filter(pin_code=code).count() == 0:
            break
    return code

def generate_qr_code():
    length = 6
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
    img = qrcode.make(code)
    img_bytes = io.BytesIO()
    img.save(img_bytes, format='PNG')
    img_base64 = base64.b64encode(img_bytes.getvalue()).decode('utf-8')
    return img_base64[:255]

class Event(models.Model):
    name = models.CharField(max_length=255)
    host = models.ForeignKey(Host, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField(default=date.today)
    queue = models.ManyToManyField(Song)
    pin_code = models.CharField(max_length=8, default=generate_event_code, unique=True, editable=False)
    qr_code = models.CharField(max_length=255, unique=True, default=generate_qr_code, editable=False)

    def __str__(self):
        return self.name