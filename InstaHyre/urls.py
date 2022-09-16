from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView
from rest_framework_swagger.views import get_swagger_view




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api.urls')),
    path('openapi/', get_schema_view(
        title="School Service",
        description="API developers hpoing to use our service"
    ), name='openapi-schema'),
    path('docs/', TemplateView.as_view(
        template_name='documentation.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='docs'),
]
