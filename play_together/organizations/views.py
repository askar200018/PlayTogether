from rest_framework.metadata import BaseMetadata, SimpleMetadata

from .models import Organization
from .serializers import OrganizationSerializerList, OrganizationSerializerDetail
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class OrganizationList(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializerList
    metadata_class = SimpleMetadata
    # permission_classes = (IsAuthenticated,)


class OrganizationDetail(generics.RetrieveAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializerDetail
