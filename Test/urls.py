from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="TEST",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.myapp.com/policies/terms/",
      contact=openapi.Contact(email="contact@test.local"),
      license=openapi.License(name="Test License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   path('admin/', admin.site.urls),
   path('api/v1/', include('poll.urls'), name='Опросы'),
   path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
