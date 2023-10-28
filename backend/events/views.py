from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Event, EventUser, SongRequest
from .serializers import EventSerializer, EventUserSerializer, SongRequestSerializer


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

class SongRequestCreateView(generics.CreateAPIView):
    queryset = SongRequest.objects.all()
    serializer_class = SongRequestSerializer

    def perform_create(self, serializer):
        song = self.request.data.get('song')
        event = self.request.data.get('event')

        existing_request = SongRequest.objects.filter(song=song, event=event, status__in=['pending', 'approved'])

        if existing_request.exists():
            raise serializers.ValidationError('This song is already requested for the event.')

        serializer.save()

class JoinEventByPIN(APIView):
    def get(self, request):
        pin_code = request.GET.get('pin')
        try:
            event = Event.objects.get(code=pin_code)
            if not event.is_active:
                return Response({'error': 'Event is not active or PIN is expired.'}, status=status.HTTP_400_BAD_REQUEST)
            serializer = EventSerializer(event)
            return Response(serializer.data)
        except Event.DoesNotExist:
            return Response({'error': 'Invalid PIN'}, status=status.HTTP_400_BAD_REQUEST)
