from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from django.utils.translation import gettext_lazy as _

from .models import User, UserActivity, LoginAttempt


@admin.register(UserActivity)
class UserActivityAdmin(admin.ModelAdmin):
    list_display = ["user"]


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (
            _("Login Credentials"),
            {
                "fields": ("email", "password"),
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "is_driver",
                    "is_vendor",
                ),
            },
        ),
        (
            _("Groups"),
            {
                "fields": (
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                ),
            },
        ),
    )

    list_display = (
        "id",
        "email",
        "is_staff",
        "is_active",
        "last_login",
    )
    list_display_links = (
        "id",
        "email",
        "is_staff",
    )
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("email",)
    ordering = ("email",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )


admin.site.register(User, UserAdmin)
