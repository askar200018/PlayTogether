from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from utils.constants import CITIES, CITY_ALMATY
import datetime


class EventQuerySet(models.QuerySet):
    def active_events(self):
        return self.filter(end_date__gte=datetime.datetime.now())

    def past_events(self):
        return self.filter(end_date__lt=datetime.datetime.now())


class Event(models.Model):
    organization = models.ForeignKey(settings.ORGANIZATION_MODEL, on_delete=models.SET_NULL, null=True)
    name = models.CharField(_('Event name'), max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=5, choices=CITIES, default=CITY_ALMATY)
    address = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    objects = EventQuerySet.as_manager()

    class Meta:
        verbose_name = (_('Event'))
        verbose_name_plural = (_('Events'))

    def __str__(self):
        return self.name


class CategoryQuerySet(models.QuerySet):
    def feature_categories(self):
        return self.filter(is_feature=True)


class Category(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, blank=True, related_name='categories')
    name = models.CharField(_('Category name'), max_length=255)
    min_age = models.PositiveSmallIntegerField(_('Minimal age'), default=0)
    max_age = models.PositiveSmallIntegerField(_('Maximal age'), default=66)
    is_feature = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name


class Court(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='courts')
    name = models.CharField(_('Court name'), max_length=255)

    class Meta:
        verbose_name = _('Court')
        verbose_name_plural = _('Courts')

    def __str__(self):
        return self.name


class Team(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='teams')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='teams')
    players = models.ManyToManyField(settings.AUTH_USER_MODEL)
    name = models.CharField(_('Team name'), max_length=255)

    class Meta:
        verbose_name = _('Team')
        verbose_name_plural = _('Teams')

    def __str__(self):
        return self.name


class Game(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='games')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='games')
    court = models.ForeignKey(Court, on_delete=models.RESTRICT, related_name='games')
    date = models.DateTimeField()
    team_a = models.ForeignKey(Team, on_delete=models.RESTRICT, related_name='team_a_games')
    team_b = models.ForeignKey(Team, on_delete=models.RESTRICT, related_name='team_b_games')

    class Meta:
        verbose_name = _('Game')
        verbose_name_plural = _('Games')


class Result(models.Model):
    game = models.OneToOneField(Game, on_delete=models.CASCADE, related_name='result')
    score_a = models.IntegerField(null=True, default=None)
    score_b = models.IntegerField(null=True, default=None)
