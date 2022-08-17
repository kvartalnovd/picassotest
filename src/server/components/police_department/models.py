from django.db import models
from components.state_structures.models import Cities


class AddressTypes(models.Model):
    address_type_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'address_types'
        verbose_name = "address type"
        verbose_name_plural = "address types"

    def __str__(self) -> str:
        return f'{self.name}'


class ServiceCalls(models.Model):
    call_id = models.IntegerField(primary_key=True)
    crime_id = models.IntegerField(unique=True)
    original_crime_type_name = models.CharField(max_length=255)
    report_date = models.DateField()
    offense_date = models.DateField()
    call_date_time = models.DateField()
    disposition = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255)
    city = models.ForeignKey(Cities, models.DO_NOTHING, db_column='city', blank=True, null=True)
    address_type = models.ForeignKey(AddressTypes, models.DO_NOTHING, db_column='address_type')
    common_location = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'service_calls'
        verbose_name = "service call"
        verbose_name_plural = "service calls"
