from django.contrib import admin
from main.models import User, Room, Profile, Nominee, Indication, Category

# Register your models here.

admin.site.register([Room, Profile, Nominee, Indication, Category])
