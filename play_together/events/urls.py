from django.urls import path
from .views import EventList, EventDetail, CategoryViewSet, CourtViewSet, TeamViewSet, GameViewSet, result_list, \
    active_events, past_events

app_name = 'events'

team_list = TeamViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

team_detail = TeamViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

game_list = GameViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

game_detail = GameViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

category_game_list = GameViewSet.as_view({
    'post': 'category_games_create',
    'get': 'category_games',
})

category_game_detail = GameViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

category_list = CategoryViewSet.as_view({
    'post': 'event_categories_create',
    'get': 'event_categories',
})

category_detail = CategoryViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

court_list = CourtViewSet.as_view({
    'post': 'event_courts_create',
    'get': 'event_courts',
})

court_detail = CourtViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

category_teams = TeamViewSet.as_view({
    'post': 'category_teams_create',
    'get': 'category_teams',
})

event_teams = TeamViewSet.as_view({
    'get': 'event_teams',
})

event_games = GameViewSet.as_view({
    'get': 'event_games',
})

url_events = [
    path('events/', EventList.as_view(), name='event_list'),
    path('events/active/', active_events, name="active_events"),
    path('events/past/', past_events, name="past_events"),
    path('events/<int:pk>/', EventDetail.as_view(), name='event_detail'),
    path('events/<int:event_id>/categories/', category_list, name="event_categories"),
    path('events/<int:event_id>/categories/<int:pk>/', category_detail, name="category_detail"),
    path('events/<int:event_id>/courts/', court_list, name="court_list"),
    path('events/<int:event_id>/courts/<int:pk>/', court_detail, name="court_detail"),
    path('events/<int:event_id>/teams/', event_teams, name="event_teams"),
    path('events/<int:event_id>/games/', event_games, name="event_games"),
]

url_categories = [
    path('categories/<int:category_id>/teams/', category_teams, name="category_teams"),
    path('categories/<int:category_id>/teams/<int:pk>/', team_detail, name="team_detail"),
    path('categories/<int:category_id>/games/', category_game_list, name="category_game_list"),
    path('categories/<int:category_id>/games/<int:pk>/', category_game_detail, name="category_game_detail"),
]

urlpatterns = [
                  path('teams/', team_list, name='team_list'),
                  path('teams/<int:pk>/', team_detail, name="team_detail"),
                  path('games/', game_list, name='game_list'),
                  path('games/<int:pk>/', game_detail, name="game_detail"),
                  path('games/<int:game_id>/result/', result_list, name="result_list"),
              ] + url_events + url_categories
