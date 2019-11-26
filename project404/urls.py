
from django.urls import path
from django.conf.urls import url

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from push_api import views

schema_view = get_schema_view(
   openapi.Info(
      title='API',
      default_version='v1',
      description='Test description'
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('messages/', views.MessageList.as_view()),
    path('messages/<int:pk>/', views.MessageDetail.as_view()),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
