from django.contrib import admin
from blog.models import *


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    class Media:
        js = ('scripts/tinyinject.js',)


admin.site.register(Category)
# Register your models here.
