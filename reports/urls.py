from django.urls import path
from . import views

urlpatterns = [

    path(
        "",
        views.reports_dashboard,
        name="reports_dashboard"
    ),

    path(
        "patients/",
        views.patient_report,
        name="patient_report"
    ),

    path(
        "doctors/",
        views.doctor_report,
        name="doctor_report"
    ),

    path(
        "appointments/",
        views.appointment_report,
        name="appointment_report"
    ),

    path("billing/", views.billing_report, name="billing_report"),
    path("monthly/", views.monthly_report, name="monthly_report"),
    path("patient/pdf/", views.patient_report_pdf, name="patient_report_pdf"),
]