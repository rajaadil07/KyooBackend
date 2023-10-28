from rest_framework import generics
from .models import Event, EventUser
from .serializers import EventSerializer, EventUserSerializer

class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventUserListCreateView(generics.ListCreateAPIView):
    queryset = EventUser.objects.all()
    serializer_class = EventUserSerializer

class EventUserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EventUser.objects.all()
    serializer_class = EventUserSerializer
