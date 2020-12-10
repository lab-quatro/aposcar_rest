from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from main.views import CustomAuthToken

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('login/', CustomAuthToken.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
