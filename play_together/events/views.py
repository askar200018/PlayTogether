from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .models import Event, Team, Game, Result, Category, Court
from .serializers import EventListSerializer, EventDetailSerializer, TeamSerializer, TeamDetailSerializer, \
    GameSerializer, GameDetailSerializer, ResultSerializer, \
    CategorySerializer, CourtSerializer
from rest_framework import generics, status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from django.shortcuts import get_object_or_404
import logging

logger = logging.getLogger(__name__)


class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventListSerializer


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer


@api_view(['GET'])
def active_events(request):
    if request.method == 'GET':
        snippets = Event.objects.active_events()
        serializer = EventListSerializer(snippets, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def past_events(request):
    if request.method == 'GET':
        snippets = Event.objects.past_events()
        serializer = EventListSerializer(snippets, many=True)
        return Response(serializer.data)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(detail=False, methods=['post'])
    def event_categories_create(self, request, event_id):
        data = request.data.copy()
        data['event'] = event_id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False, methods=['get'])
    def event_categories(self, request, event_id):
        queryset = Event.objects.all()
        event = get_object_or_404(queryset, pk=event_id)
        serializer = self.get_serializer(event.categories, many=True)
        return Response(serializer.data)


class CourtViewSet(viewsets.ModelViewSet):
    queryset = Court.objects.all()
    serializer_class = CourtSerializer

    @action(detail=False, methods=['post'])
    def event_courts_create(self, request, event_id):
        data = request.data.copy()
        data['event'] = event_id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False, methods=['get'])
    def event_courts(self, request, event_id):
        queryset = Event.objects.all()
        event = get_object_or_404(queryset, pk=event_id)
        serializer = self.get_serializer(event.courts, many=True)
        return Response(serializer.data)


class TeamViewSet(viewsets.ModelViewSet):
    # queryset = Team.objects.all()
    # serializer_class = TeamSerializer

    # permission_classes = (IsAuthenticatedOrReadOnly,)
    def get_queryset(self):
        queryset = Team.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return TeamDetailSerializer
        elif self.action == 'retrieve':
            return TeamDetailSerializer
        elif self.action == 'event_teams':
            return TeamDetailSerializer
        elif self.action == 'category_teams':
            return TeamDetailSerializer
        return TeamSerializer

    @action(detail=False, methods=['post'])
    def category_teams_create(self, request, category_id):
        data = request.data.copy()
        queryset = Category.objects.all()
        category = get_object_or_404(queryset, pk=category_id)
        data['event'] = category.event_id
        data['category'] = category.pk
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False, methods=['get'])
    def event_teams(self, request, event_id):
        queryset = Event.objects.all()
        event = get_object_or_404(queryset, pk=event_id)
        serializer = self.get_serializer(event.teams, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def category_teams(self, request, category_id):
        queryset = Category.objects.all()
        category = get_object_or_404(queryset, pk=category_id)
        serializer = self.get_serializer(category.teams, many=True)
        return Response(serializer.data)


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return GameDetailSerializer
        elif self.action == 'retrieve':
            return GameDetailSerializer
        elif self.action == 'event_games':
            return GameDetailSerializer
        elif self.action == 'category_games':
            return GameDetailSerializer
        return GameSerializer

    @action(detail=False, methods=['post'])
    def category_games_create(self, request, category_id):
        data = request.data.copy()
        queryset = Category.objects.all()
        category = get_object_or_404(queryset, pk=category_id)
        data['event'] = category.event_id
        data['category'] = category.pk
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False, methods=['get'])
    def event_games(self, request, event_id):
        queryset = Event.objects.all()
        event = get_object_or_404(queryset, pk=event_id)
        serializer = self.get_serializer(event.games, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def category_games(self, request, category_id):
        queryset = Category.objects.all()
        category = get_object_or_404(queryset, pk=category_id)
        serializer = self.get_serializer(category.games, many=True)
        return Response(serializer.data)


class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer


@api_view(['POST'])
def result_list(request, game_id):
    if request.method == 'POST':
        data = request.data.copy()
        data['game'] = game_id
        serializer = ResultSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error(f'Result object serializer is not valid, ID: {serializer.instance}')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
