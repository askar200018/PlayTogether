from django.core.validators import EmailValidator
from rest_framework import serializers
from auth_.serializers import MainUserSerializer

from utils.constants import CITIES


class OrganizationBaseSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField(required=True, validators=[EmailValidator])
    phone_number = serializers.CharField(max_length=255)
    website = serializers.URLField()
    city = serializers.ChoiceField(choices=CITIES, source='get_city_display')
    contact_first_name = serializers.CharField(max_length=255)
    contact_last_name = serializers.CharField(max_length=255)
    created_date = serializers.DateField(read_only=True)


class OrganizationSerializerList(OrganizationBaseSerializer):
    owner_id = serializers.IntegerField()


class OrganizationSerializerDetail(OrganizationBaseSerializer):
    owner = MainUserSerializer(read_only=True)
