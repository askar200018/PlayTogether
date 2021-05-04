from django.urls import path
from .views import OrganizationList, OrganizationDetail

app_name = 'organizations'

urlpatterns = [
    path('organizations/', OrganizationList.as_view(), name='organization_list'),
    path('organizations/<int:pk>/', OrganizationDetail.as_view(), name='organization_detail'),
]
