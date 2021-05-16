from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from .serializers import RegisterUserSerializer
from .models import MainUser
import logging

logger = logging.getLogger(__name__)


class UserCreate(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = MainUser.objects.all()
    serializer_class = RegisterUserSerializer

    # def post(self, request, *args, **kwargs):
    #     return self.create(request, args, kwargs)

    # def post(self, request):
    #     serializer = RegisterUserSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def user_list(request):
    if request.method == 'POST':
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error(f'User object serializer is not valid, ID: {serializer.instance}')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
