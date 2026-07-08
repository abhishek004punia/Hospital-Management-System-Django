from django.shortcuts import render

from patients.models import Patient
from doctors.models import Doctor
from appointments.models import Appointment
from billing.models import Billing
from django.db.models import Q


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

def doctor_report(request):

    doctors = Doctor.objects.all()

    return render(
        request,
        "reports/doctor_report.html",
        {
            "doctors": doctors
        }
    )

def appointment_report(request):

    appointments = Appointment.objects.all()

    search_date = request.GET.get("date")

    if search_date:
        appointments = appointments.filter(
            appointment_date=search_date
        )

    return render(
        request,
        "reports/appointment_report.html",
        {
            "appointments": appointments,
            "search_date": search_date,
        }
    )

def billing_report(request):

    bills = Billing.objects.all()

    total_revenue = sum(bill.total_amount for bill in bills)

    paid_bills = bills.filter(payment_status="Paid").count()

    pending_bills = bills.filter(payment_status="Pending").count()

    context = {

        "bills": bills,
        "total_revenue": total_revenue,
        "paid_bills": paid_bills,
        "pending_bills": pending_bills,

    }

    return render(
        request,
        "reports/billing_report.html",
        context
    )