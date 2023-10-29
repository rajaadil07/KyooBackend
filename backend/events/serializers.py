from rest_framework import serializers
from .models import Event, EventUser, SongRequest
from songs.serializers import SongSerializer

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class EventUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventUser
        fields = '__all__'

class SongRequestSerializer(serializers.ModelSerializer):
    song = SongSerializer()
    class Meta:
        model = SongRequest
        fields = '__all__'
