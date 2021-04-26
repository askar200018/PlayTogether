from django.contrib import admin

from .models import Event, Category, Team, Result, Court, Game


# class CategoryInline(admin.TabularInline):
#     model = Category
#
#
# class TeamInline(admin.TabularInline):
#     model = Team
#
#
# class CourtInline(admin.TabularInline):
#     model = Court
#
#
# @admin.register(Event)
# class EventAdmin(admin.ModelAdmin):
#     inlines = [
#         CategoryInline,
#         TeamInline,
#         CourtInline
#     ]
#
#
# class TeamWithScoreInline(admin.TabularInline):
#     model = TeamWithScore

admin.site.register(Event)
admin.site.register(Category)
admin.site.register(Court)
admin.site.register(Team)
admin.site.register(Game)
admin.site.register(Result)
