from django.contrib import admin
from AppBom import models

@admin.register(models.State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    list_filter = ['name']


@admin.register(models.Zone)
class ZoneAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    list_filter = ['name']


@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'state']
    search_fields = ['name']
    list_filter = ['name', 'state']