from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from evaluation_platform.users.models import CustomUser, Department, Organization


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = (
        "email",
        "first_name",
        "last_name",
        "department",
        "job_title",
        "is_manager",
        "is_staff",
        "is_active",
        "years_of_service",
    )
    list_filter = ("email", "is_staff", "is_active", "department", "role")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Personal info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "department",
                    "job_title",
                    "role",
                    "date_hired",
                )
            },
        ),
        (
            "Permissions",
            {"fields": ("is_staff", "is_active", "groups", "user_permissions")},
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
                    "first_name",
                    "last_name",
                    "department",
                    "job_title",
                    "supervisor",
                    "role",
                    "date_hired",
                    "is_staff",
                    "is_active",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )
    search_fields = ("email", "first_name", "last_name", "department")
    ordering = ("email",)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "abbreviation", "organization")


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "abbreviation",
    )


admin.site.register(CustomUser, CustomUserAdmin)
