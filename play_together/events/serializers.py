from .models import Event
from rest_framework import serializers


class EventBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'name', 'description', 'start_date', 'end_date', 'location', 'address', 'is_active')


class EventListSerializer(EventBaseSerializer):
    organization_id = serializers.IntegerField()

    class Meta(EventBaseSerializer.Meta):
        model = Event
        fields = EventBaseSerializer.Meta.fields + ('organization_id',)
