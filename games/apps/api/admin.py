from django.contrib import admin
from apps.api.models import System
from apps.api.models import Games

# Register your models here.

admin.site.register(System)
admin.site.register(Games)