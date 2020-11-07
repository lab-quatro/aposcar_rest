from django.conf.urls import url
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from main import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Aposcar API",
      default_version='v1',
      description="Provide access to all the resources of the Aposcar Project",
      contact=openapi.Contact(email="labqua4tro@gmail.com"),
   ),
   public=True,
   permission_classes=(permissions.IsAdminUser,),
)

router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='userprofile')
router.register(r'indications', views.IndicationViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'nominees', views.NomineeViewSet)
router.register(r'rooms', views.RoomViewSet)

urlpatterns = [
    path('', include(router.urls)),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
