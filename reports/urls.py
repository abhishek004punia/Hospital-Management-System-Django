from django.urls import path
from . import views

urlpatterns = [

    path("", views.reports_dashboard, name="reports_dashboard"),

    path("patients/", views.patient_report, name="patient_report"),

    path("doctors/", views.doctor_report, name="doctor_report"),

    path("appointments/", views.appointment_report, name="appointment_report"),

    path("billing/", views.billing_report, name="billing_report"),
    
    path("monthly/", views.monthly_report, name="monthly_report"),
    
    path("patient/pdf/", views.patient_report_pdf, name="patient_report_pdf"),
    
    path("doctor/pdf/", views.doctor_report_pdf, name="doctor_report_pdf"),
    
    path("appointment/pdf/", views.appointment_report_pdf, name="appointment_report_pdf"),
    
    path("billing/pdf/", views.billing_report_pdf, name="billing_report_pdf"),
    
    path("departments/", views.department_report, name="department_report"),
    
    path("department/pdf/", views.department_report_pdf, name="department_report_pdf"),
    
    path("analytics/", views.analytics_dashboard, name="analytics_dashboard"),
    
    path("pharmacy/", views.pharmacy_report, name="pharmacy_report"),
    
    path("laboratory/", views.laboratory_report, name="laboratory_report"),
    
    path("pharmacy/pdf/", views.pharmacy_report_pdf, name="pharmacy_report_pdf"),
    
    path("monthly/pdf/", views.monthly_report_pdf, name="monthly_report_pdf"),

    path("analytics/pdf/", views.analytics_pdf, name="analytics_pdf"),
]
