from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.contrib import admin
from django.urls import path, include


schema_view = get_schema_view(
    openapi.Info(
        title="Pizza Delivery API",
        default_version='v1',
        description="A REST API FOR for a Pizza delivery service",
        contact=openapi.Contact(email="contact@snippets.local"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('orders/', include('orders.urls')),

    # JWT URL
    path('auth/', include('djoser.urls.jwt')),

    # Swagger URLs
    path('swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
