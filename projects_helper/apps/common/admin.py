from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from projects_helper.apps.common.models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('user_type',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
