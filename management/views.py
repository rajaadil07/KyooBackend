from rest_framework.response import Response
from rest_framework import generics, status

from .models import Event
from permissions import IsStaffPermission
from .serializers import EventSerializer

class EventAPIView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsStaffPermission]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        event = serializer.save()

        return Response({'message': 'Event created successfully'}, status=status.HTTP_201_CREATED)