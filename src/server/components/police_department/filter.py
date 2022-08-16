from django_filters import rest_framework as filters

from components.police_department import models


class ServiceCallsFilter(filters.FilterSet):
    date = filters.DateTimeFromToRangeFilter(field_name='report_date')

    class Meta:
        model = models.ServiceCalls
        fields = ['date']
