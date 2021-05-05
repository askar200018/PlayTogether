from .permissions import IsOwnerOrIsAuthenticated
from .models import Organization
from .serializers import OrganizationSerializerList, OrganizationSerializerDetail
from rest_framework.metadata import SimpleMetadata
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response


class OrganizationList(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializerList
    metadata_class = SimpleMetadata
    permission_classes = (IsOwnerOrIsAuthenticated,)

    # def list(self, request, *args, **kwargs):
    #     queryset = Organization.objects.owner_organizations(user=self.request.user)
    #     serializer = OrganizationSerializerList(queryset, many=True)
    #     return Response(serializer.data)

    def get_queryset(self):
        user = self.request.user
        return Organization.objects.owner_organizations(user)


class OrganizationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializerDetail
    permission_classes = (IsOwnerOrIsAuthenticated,)


