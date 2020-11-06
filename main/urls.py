from django.urls import include, path
from rest_framework.routers import DefaultRouter
from main import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='userprofile')
router.register(r'indications', views.IndicationViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'nominees', views.NomineeViewSet)
router.register(r'rooms', views.RoomViewSet)

urlpatterns = [
    path('', include(router.urls))
]
