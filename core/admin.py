from django.contrib import admin
from core.models import Room, Nominee, Indication, Category, UserProfile

# Register your models here.

admin.site.register([Room, Nominee, Indication, Category, UserProfile])
