from django.shortcuts import render

from patients.models import Patient
from doctors.models import Doctor
from appointments.models import Appointment


def login_view(request):
    return render(request, 'accounts/login.html')


def dashboard(request):

    total_patients = Patient.objects.count()

    total_doctors = Doctor.objects.count()

    total_appointments = Appointment.objects.count()

    pending_appointments = Appointment.objects.filter(
        status="Pending"
    ).count()

    context = {

        "total_patients": total_patients,

        "total_doctors": total_doctors,

        "total_appointments": total_appointments,

        "pending_appointments": pending_appointments,

    }

    return render(
        request,
        "dashboard/dashboard.html",
        context
    )
