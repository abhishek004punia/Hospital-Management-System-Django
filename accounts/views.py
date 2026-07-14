from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from patients.models import Patient
from doctors.models import Doctor
from appointments.models import Appointment
from billing.models import Billing
from departments.models import Department
from users.forms import LoginForm
from django.http import HttpResponseForbidden
from pharmacy.models import Medicine
from django.db.models import Q
from laboratory.models import LabTest
from .decorators import admin_required


def login_view(request):

    message = ""

    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user is not None:

                login(request, user)

                if user.groups.filter(name="Admin").exists():
                    return redirect("dashboard")

                elif user.groups.filter(name="Doctor").exists():
                    return redirect("doctor_dashboard")

                elif user.groups.filter(name="Receptionist").exists():
                    return redirect("reception_dashboard")

                else:
                    logout(request)
                    message = "No role assigned to this user."

            
    return render(
        request,
        "accounts/login.html",
        {
            "form": form,
            "message": message,
        }
    )


@login_required(login_url="/users/login/")
@admin_required
def dashboard(request):

    print("Logged in user:", request.user.username)
    print("Groups:", list(request.user.groups.values_list("name", flat=True)))

    if not request.user.groups.filter(name="Admin").exists():
        return HttpResponseForbidden("Access Denied")

    # Dashboard Statistics
    total_patients = Patient.objects.count()
    total_doctors = Doctor.objects.count()
    total_appointments = Appointment.objects.count()
    total_departments = Department.objects.count()
    total_medicines = Medicine.objects.count()
    low_stock_count = Medicine.objects.filter(stock__lt=20).count()
    total_lab_tests = LabTest.objects.count()

    pending_appointments = Appointment.objects.filter(
        status="Pending"
    ).count()

    # Recent Patients
    recent_patients = Patient.objects.order_by("-id")[:5]

    # Today's Appointments
    today = timezone.localdate()

    today_appointments = Appointment.objects.order_by(
        "-appointment_date",
        "-appointment_time"
    )[:5]

    # Recent Bills
    recent_bills = Billing.objects.order_by("-id")[:5]

    # Notifications
    notifications = [
    {"icon": "🟢", "message": "New Patient Registered"},
    {"icon": "👨‍⚕️", "message": "Doctor Added"},
    {"icon": "📅", "message": "Appointment Booked"},
    {"icon": "💳", "message": "Bill Generated"},
    {"icon": "🏢", "message": "Department Added"},
    {"icon": "💊", "message": "Medicine Added"},
    {"icon": "🧪", "message": "Lab Test Added"},
    {"icon": "📋", "message": "Prescription Created"},
    {"icon": "📊", "message": "Reports Generated"},
]

    # Recent Activity
    activities = [
        {
            "time": "09:15 AM",
            "message": "New Patient Registered",
            "color": "success",
        },
        {
            "time": "09:40 AM",
            "message": "Doctor Added",
            "color": "primary",
        },
        {
            "time": "10:00 AM",
            "message": "Appointment Booked",
            "color": "warning",
        },
        {
            "time": "10:30 AM",
            "message": "Bill Generated",
            "color": "info",
        },
        {
            "time": "11:00 AM",
            "message": "Department Added",
            "color": "secondary",
        },
        {
            "time": "11:20 AM",
            "message": "Medicine Added",
            "color": "success",
        },
        {
            "time": "11:45 AM",
            "message": "Lab Test Added",
            "color": "danger",
        },
        {
            "time": "12:00 PM",
            "message": "Reports Generated",
            "color": "dark",
        },
    ]

    context = {
        "total_patients": total_patients,
        "total_doctors": total_doctors,
        "total_appointments": total_appointments,
        "total_departments": total_departments,
        "total_medicines": total_medicines,
        "low_stock_count": low_stock_count,
        "pending_appointments": pending_appointments,
        "recent_patients": recent_patients,
        "today_appointments": today_appointments,
        "recent_bills": recent_bills,
        "notifications": notifications,
        "activities": activities,
        "total_lab_tests": total_lab_tests,
    }

    return render(
        request,
        "dashboard/dashboard.html",
        context
    )


def logout_view(request):

    logout(request)

    return redirect("/")    