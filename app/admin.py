from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from . models import User, Role

class UserAdmin(BaseException):
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )
    
admin.site.register(User, BaseUserAdmin)
admin.site.register(Role)