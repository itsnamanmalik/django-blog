from django.contrib import admin
from video.models import *

# Register your models here.

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    class Media:
        js = ('scripts/tinyinject.js',)
