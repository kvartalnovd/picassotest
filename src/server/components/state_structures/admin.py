from django.contrib import admin

from . import models


@admin.register(models.States)
class StatesAdmin(admin.ModelAdmin):
    list_display = ('state_id', 'name')


@admin.register(models.Cities)
class CitiesAdmin(admin.ModelAdmin):
    list_display = ('city_id', 'name', 'state')
