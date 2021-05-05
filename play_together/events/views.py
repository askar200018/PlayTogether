from .models import Event, Team
from .serializers import EventListSerializer, TeamSerializer
from rest_framework import generics
from rest_framework import viewsets


class EventList(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventListSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
