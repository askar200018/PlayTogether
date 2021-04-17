from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager
from django_countries.fields import CountryField
from utils.constants import GENDER_CHOICES


class MainUserManager(BaseUserManager):
    def create_superuser(self, email, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, password, **other_fields)

    def create_user(self, email, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email,
                          **other_fields)
        user.set_password(password)
        user.save()
        return user


class MainUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), max_length=255, unique=True)
    phone_number = models.CharField(max_length=20, blank=True)
    first_name = models.CharField(_('first name'), max_length=150, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    nationality = CountryField(_('nationality'), blank=True)
    gender = models.CharField(
        max_length=2,
        choices=GENDER_CHOICES,
        blank=True
    )
    points = models.IntegerField(default=0)
    profile_image = models.ImageField(
        verbose_name=_('profile image'),
        help_text=_('Upload image to profile'),
        upload_to='posts/%Y/%m/%d/',
        default='posts/default.png')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = MainUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return '{}:{}'.format(self.first_name, self.last_name)
