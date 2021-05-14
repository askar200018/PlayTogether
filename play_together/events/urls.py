from django.urls import path
from .views import EventList, EventDetail, TeamViewSet, GameViewSet

app_name = 'events'

urlpatterns = [
    path('events/', EventList.as_view(), name='event_list'),
    path('events/<int:pk>/', EventDetail.as_view(), name='event_detail'),
    path('teams/', TeamViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }), name='teams_list'),
    path('games/', GameViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name="game_view_set")
]
