from django.urls import path
from .views import UserCreate, user_list

app_name = 'auth_'

urlpatterns = [
    path('register/', user_list, name='create_user'),
]
