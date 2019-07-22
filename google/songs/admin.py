from django.contrib import admin

# Register your models here.
from .models import Songs, SongsFixed

admin.site.register(Songs)
admin.site.register(SongsFixed)