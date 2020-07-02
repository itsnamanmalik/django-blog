from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from accounts.models import *

# Register your models here.
class AccountAdmin(UserAdmin):
	list_display = ('email','username','date_joined', 'last_login', 'is_admin','is_staff')
	search_fields = ('email','username',)
	readonly_fields=('date_joined', 'last_login')
	
	filter_horizontal = ()
	list_filter = ('is_staff', 'is_admin', 'is_superuser')
	fieldsets = (
		(None, {
            'fields': ('password', 'email', 'username', 'profile_pic')
        }),
		('Important Dates', {
            
            'fields': ('date_joined', 'last_login'),
        }),
		('Permissions', {
            'classes': ('collapse',),
            'fields': ('is_active', 'is_admin', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),  
	)

admin.site.register(Account, AccountAdmin)