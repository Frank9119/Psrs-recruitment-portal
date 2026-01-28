from django.contrib import admin
from psrs_auth.models import User, UserProfile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin







# Register your models here.
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    search_fields = ["first_name", "last_name", "email", "username"]
    list_display = ["username", "first_name", "last_name", "email", "role"]
    list_filter = ["role", "first_name", "last_name"]

    


    ordering = ["email"]

