from django.contrib import admin
from .models import Patient
# Register your models here.

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = (
        "patient_id",
        "full_name",
        "age",
        "gender",
        "mobile",
        "disease",
    )

    search_fields = (
        "patient_id",
        "full_name",
        "mobile",
    )

    list_filter = (
        "gender",
        "blood_group",
    )