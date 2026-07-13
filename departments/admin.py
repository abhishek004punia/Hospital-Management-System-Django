from django.contrib import admin
from .models import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = (
        "department_id",
        "department_name",
        "department_head",
        "location",
        "created_at",
    )

    search_fields = (
        "department_name",
        "department_head",
        "location",
    )

    list_filter = (
        "location",
        "created_at",
    )

    ordering = ("department_name",)