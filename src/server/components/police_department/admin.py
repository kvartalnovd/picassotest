from django.contrib import admin

from . import models


@admin.register(models.AddressTypes)
class AddressTypesAdmin(admin.ModelAdmin):
    list_display = ('address_type_id', 'name')


@admin.register(models.ServiceCalls)
class ServiceCallsAdmin(admin.ModelAdmin):
    list_display = ('report_date', 'offense_date', 'call_date_time', 'disposition', 'address', 'city')
