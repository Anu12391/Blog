from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from login.models import NewUser




class NewUserAdminConfig(UserAdmin):
    ordering = ['joining_date']

    list_display = [ 'joining_date', 'email', 'first_name','last_name','is_staff','is_superuser','is_active']




# Register your models here.
admin.site.register(NewUser,NewUserAdminConfig)
