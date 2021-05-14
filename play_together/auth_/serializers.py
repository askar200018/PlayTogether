from django.core.validators import EmailValidator
from django_countries.serializer_fields import CountryField
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from utils.constants import GENDER_CHOICES
from .models import MainUser, Profile


class ProfileSerializer(serializers.Serializer):
    location = serializers.CharField()
    hometown = serializers.CharField()

    def create(self, validated_data):
        return Profile.objects.create(**validated_data)


class RegisterUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True,
                                   validators=[UniqueValidator(queryset=MainUser.objects.all()), EmailValidator, ])
    password = serializers.CharField(min_length=4, write_only=True)

    # gender = serializers.ChoiceField(choices=GENDER_CHOICES, source='get_gender_display')
    # nationality = CountryField(name_only=True)

    class Meta:
        model = MainUser
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}, }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class MainUserSerializer(serializers.ModelSerializer):
    gender = serializers.ChoiceField(choices=GENDER_CHOICES, source='get_gender_display')
    nationality = CountryField(name_only=True)

    class Meta:
        model = MainUser
        fields = ('email', 'phone_number', 'first_name', 'last_name', 'date_of_birth', 'nationality', 'gender')


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainUser
        fields = ('id', 'first_name', 'last_name',)
