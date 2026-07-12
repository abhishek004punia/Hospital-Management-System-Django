from django.contrib import admin
from .models import Doctor


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "specialization",
        "department",
        "mobile",
        "status",
    )

    search_fields = (
        "full_name",
        "specialization",
        "department",
    )

    list_filter = (
        "department",
        "status",
        "gender",
    )

    ordering = ("full_name",)