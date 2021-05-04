from django.core.validators import EmailValidator
from rest_framework import serializers
from auth_.serializers import MainUserSerializer
from .models import Organization

from utils.constants import CITIES


class OrganizationBaseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    email = serializers.EmailField(required=True, validators=[EmailValidator])
    phone_number = serializers.CharField(max_length=255)
    website = serializers.URLField(required=False)
    city = serializers.ChoiceField(choices=CITIES)
    contact_first_name = serializers.CharField(max_length=255)
    contact_last_name = serializers.CharField(max_length=255)
    created_date = serializers.DateField(read_only=True)

    def create(self, validated_data):
        return Organization.objects.create(**validated_data)


class OrganizationSerializerList(OrganizationBaseSerializer):
    owner_id = serializers.IntegerField(required=False)

    def create(self, validated_data):
        validated_data['owner_id'] = self.context.get('request').user.id
        # owner_id = self.context.get('request').user.id
        return super().create(validated_data)




class OrganizationSerializerDetail(OrganizationBaseSerializer):
    owner = MainUserSerializer(read_only=True)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.website = validated_data.get('website', instance.website)
        instance.city = validated_data.get('city', instance.city)
        instance.contact_first_name = validated_data.get('contact_first_name', instance.contact_first_name)
        instance.save()
        return instance
