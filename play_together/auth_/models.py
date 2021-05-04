from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django_countries.fields import CountryField
from utils.constants import GENDER_CHOICES


class MainUserManager(BaseUserManager):

    # def _create_user(self, email, password, **extra_fields):
    #     """
    #     Creates and saves a User with the given email and password.
    #     """
    #     if not email:
    #         raise ValueError('The given email must be set')
    #     email = self.normalize_email(email)
    #     user = self.model(email=email, **extra_fields)
    #     user.set_password(password)
    #     user.save(using=self._db)
    #     return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
                Creates and saves a superuser with the given email, date of
                birth and password.
        """
        user = self.create_user(email, password=password, **extra_fields)
        # extra_fields.setdefault('is_staff', True)
        # extra_fields.setdefault('is_superuser', True)
        # extra_fields.setdefault('is_active', True)
        #
        # if extra_fields.get('is_staff') is not True:
        #     raise ValueError(
        #         'Superuser must be assigned to is_staff=True.')
        # if extra_fields.get('is_superuser') is not True:
        #     raise ValueError('Superuser must have is_superuser=True.')
        user.is_admin = True
        user.save(using=self.db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """
                Creates and saves a User with the given email, date of
                birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            **extra_fields,
        )

        user.set_password(password)
        user.save(using=self._db)
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
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = MainUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        # Simplest possible answer: All admins are staff
        return self.is_admin
