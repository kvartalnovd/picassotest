from rest_framework import serializers

from components.police_department import models


class ServiceCallsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ServiceCalls
        fields = ('call_id', 'crime_id', 'original_crime_type_name', 'report_date', 'offense_date', 'call_date_time',
                  'disposition', 'address', 'city', 'address_type', 'common_location')
