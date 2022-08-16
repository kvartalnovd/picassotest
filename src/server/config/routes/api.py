from django.conf import settings
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from components.police_department.endpoint.views import ServiceCallsListView


schema_view = get_schema_view(
    openapi.Info(
        title='Test assignment to the company "Picasso Software"',
        default_version='v1',
        description="application based on Django 4.0 & Django REST Framework",
        contact=openapi.Contact(url="https://picasso.io/team/contact")
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

urlpatterns = [
    # Django REST Framework authentication
    path('auth/', include('rest_framework.urls')),

    # Police Services
    path('service-calls', ServiceCallsListView.as_view())
]

if settings.DEBUG:
    urlpatterns += [
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]