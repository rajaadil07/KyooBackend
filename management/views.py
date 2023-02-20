from rest_framework import generics
from .models import Event
from .serializers import EventSerializer
from rest_framework.response import Response

class EventAPIView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer