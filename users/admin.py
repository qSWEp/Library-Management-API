from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("User info", {"fields": ("role", "phone")}),
    )
    
    list_display = UserAdmin.list_display + (
        'role', 'phone',
    )
    #filter for roles
    list_filter = UserAdmin.list_filter + (
        'role',
    )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("User info", {"classes": ("wide",), "fields":("email", "phone", "first_name", "last_name")}),
    )

