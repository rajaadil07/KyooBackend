from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    queue = serializers.StringRelatedField(many=True)
    host = serializers.CharField(source='host.display_name')
    class Meta:
        model = Event
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        queue = instance.queue.all()
        representation['queue'] = [song.__str__() for song in queue]
        return representation