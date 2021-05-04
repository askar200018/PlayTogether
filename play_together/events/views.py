from .models import Event
from .serializers import EventListSerializer
from rest_framework import generics


class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventListSerializer
