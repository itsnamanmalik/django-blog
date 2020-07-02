from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from home.models import *

# Register your models here.
admin.site.site_header='Mad Learners Admin'
admin.site.site_title = 'Mad Learners'

# admin.site.register(ProfileInfo)
admin.site.register(ContactForm)