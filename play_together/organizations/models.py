from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from utils.constants import CITIES, CITY_ALMATY


class OrganizationQuerySet(models.QuerySet):
    def owner_organizations(self, user):
        return self.filter(owner=user)


class Organization(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='organizations')
    name = models.CharField(_('Organization name'), max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    website = models.URLField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=5, choices=CITIES)
    contact_first_name = models.CharField(max_length=255)
    contact_last_name = models.CharField(max_length=255)
    created_date = models.DateField(auto_now_add=True)

    objects = OrganizationQuerySet.as_manager()

    class Meta:
        verbose_name = _('Organization')
        verbose_name_plural = _('Organizations')

    def __str__(self):
        return self.name
