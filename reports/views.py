from django.shortcuts import render

from patients.models import Patient
from doctors.models import Doctor
from appointments.models import Appointment
from billing.models import Billing


def reports_dashboard(request):

    context = {

        "total_patients": Patient.objects.count(),

        "total_doctors": Doctor.objects.count(),

        "total_appointments": Appointment.objects.count(),

        "total_bills": Billing.objects.count(),

    }

    return render(
        request,
        "reports/dashboard_reports.html",
        context
    )


def patient_report(request):

    patients = Patient.objects.all()

    return render(
        request,
        "reports/patient_report.html",
        {
            "patients": patients
        }
    )