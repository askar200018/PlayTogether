from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from utils.constants import CITIES, CITY_ALMATY


class Event(models.Model):
    organizer = models.ForeignKey(settings.ORGANIZATION_MODEL, on_delete=models.SET_NULL, null=True)
    name = models.CharField(_('Event name'), max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=5, choices=CITIES, default=CITY_ALMATY)
    address = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = (_('Event'))
        verbose_name_plural = (_('Events'))

    def __str__(self):
        return self.name


class Category(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, blank=True, related_name='categories')
    name = models.CharField(_('Category name'), max_length=255)
    is_feature = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name


class Team(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='teams')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    player = models.ManyToManyField(settings.AUTH_USER_MODEL)
    name = models.CharField(_('Team name'), max_length=255)

    class Meta:
        verbose_name = _('Team')
        verbose_name_plural = _('Teams')

    def __str__(self):
        return self.name


class Court(models.Model):
    name = models.CharField(_('Court name'), max_length=255)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='courts')

    class Meta:
        verbose_name = _('Court')
        verbose_name_plural = _('Courts')

    def __str__(self):
        return self.name


class TeamWithScore(models.Model):
    team = models.OneToOneField(Team, on_delete=models.RESTRICT)
    score = models.IntegerField(default=0)

    class Meta:
        verbose_name = _('TeamWithScore')
        verbose_name_plural = _('TeamsWithScore')


class Game(models.Model):
    first_team = models.ForeignKey(TeamWithScore, on_delete=models.RESTRICT, related_name='first_team_games')
    second_team = models.ForeignKey(TeamWithScore, on_delete=models.RESTRICT, related_name='second_team_games')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='games')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='games')
    court = models.ForeignKey(Court, on_delete=models.RESTRICT, related_name='games')
    date = models.DateTimeField()

    class Meta:
        verbose_name = _('Game')
        verbose_name_plural = _('Games')
