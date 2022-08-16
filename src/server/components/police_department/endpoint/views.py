from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, parsers, generics, permissions

from components.police_department import serializer, models
from components.police_department.filter import ServiceCallsFilter


class ServiceCallsListView(generics.ListAPIView):
    """ Viewing and editing user data """

    queryset = models.ServiceCalls.objects.order_by('-report_date')
    serializer_class = serializer.ServiceCallsSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ServiceCallsFilter
