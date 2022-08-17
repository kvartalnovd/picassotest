from django.contrib import admin

from . import models


@admin.register(models.AddressTypes)
class AddressTypesAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(models.ServiceCalls)
class ServiceCallsAdmin(admin.ModelAdmin):
    list_display = ('crime_id', 'report_date', 'offense_date', 'call_date_time',
                    'disposition', 'city', 'address', 'common_location')
