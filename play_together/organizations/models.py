from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from utils.constants import CITIES, CITY_ALMATY


class Organization(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(_('Organization name'), max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    website = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=5, choices=CITIES)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    class Meta:
        verbose_name = _('Organization')
        verbose_name_plural = _('Organizations')

    def __str__(self):
        return self.name