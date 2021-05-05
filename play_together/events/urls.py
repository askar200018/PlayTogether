from django.urls import path
from .views import EventList, TeamViewSet

app_name = 'events'

urlpatterns = [
    path('events/', EventList.as_view({
        'get': 'list',
        'post': 'create',
    }), name='event_list'),
    path('teams/', TeamViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }), name='teams_list')
]
