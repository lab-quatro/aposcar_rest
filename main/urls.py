from django.urls import include, path
from rest_framework.routers import DefaultRouter
from main import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'indications', views.IndicationViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'nominees', views.NomineeViewSet)

urlpatterns = [
    path('', include(router.urls))
]
