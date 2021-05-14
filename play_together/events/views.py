from .models import Event, Team, Game, Result
from .serializers import EventListSerializer, EventDetailSerializer, TeamSerializer, GameSerializer
from rest_framework import generics
from rest_framework import viewsets


class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventListSerializer


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer


# class EventList(viewsets.ModelViewSet):
#     queryset = Event.objects.all()
#     serializer_class = EventListSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
