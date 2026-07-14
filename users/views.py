from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from patients.models import Patient
from appointments.models import Appointment
from prescriptions.models import Prescription
from laboratory.models import LabTest
from billing.models import Billing
from pharmacy.models import Medicine
from django.utils import timezone
from accounts.decorators import doctor_required
from accounts.decorators import receptionist_required



def login_view(request):

    form = LoginForm()
    message = ""

    if request.method == "POST":

        form = LoginForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(
                request,
                username=username,
                password=password,
            )

            if user is not None:

                login(request, user)

                if user.groups.filter(name="Admin").exists():
                    return redirect("/dashboard/")

                elif user.groups.filter(name="Doctor").exists():
                    return redirect("/users/doctor-dashboard/")

                elif user.groups.filter(name="Receptionist").exists():
                    return redirect("/users/reception-dashboard/")

                else:
                    return redirect("/users/login/")

            else:
                message = "Invalid Username or Password"

    return render(
        request,
        "users/login.html",
        {
            "form": form,
            "message": message,
        }
    )


def logout_view(request):

    logout(request)

    return redirect("/users/login/")

@login_required
@doctor_required
def doctor_dashboard(request):

    today = timezone.localdate()

    # Notifications
    notifications = [
        {"icon": "📋", "message": "Prescription Created"},
        {"icon": "🧪", "message": "Lab Test Added"},
        {"icon": "📅", "message": "Appointment Booked"},
        {"icon": "👥", "message": "New Patient Registered"},
    ]

    # Recent Activity
    activities = [
        {
            "time": "09:00 AM",
            "message": "Prescription Created",
            "color": "success",
        },
        {
            "time": "09:45 AM",
            "message": "Lab Test Added",
            "color": "danger",
        },
        {
            "time": "10:30 AM",
            "message": "Appointment Booked",
            "color": "warning",
        },
        {
            "time": "11:15 AM",
            "message": "Patient Checked",
            "color": "primary",
        },
    ]

    context = {
        "total_patients": Patient.objects.count(),
        "total_appointments": Appointment.objects.count(),
        "total_prescriptions": Prescription.objects.count(),
        "total_lab_tests": LabTest.objects.count(),

        "today_appointments": Appointment.objects.filter(
            appointment_date=today
        ).order_by("appointment_time")[:5],

        "recent_prescriptions": Prescription.objects.order_by("-id")[:5],

        "notifications": notifications,
        "activities": activities,
    }

    return render(
        request,
        "users/doctor_dashboard.html",
        context,
    )


@login_required
@receptionist_required
def reception_dashboard(request):

    today = timezone.localdate()

    # Notifications
    notifications = [
        {"icon": "🟢", "message": "New Patient Registered"},
        {"icon": "📅", "message": "Appointment Booked"},
        {"icon": "💳", "message": "Bill Generated"},
        {"icon": "💊", "message": "Medicine Issued"},
    ]

    # Recent Activity
    activities = [
        {
            "time": "09:15 AM",
            "message": "New Patient Registered",
            "color": "success",
        },
        {
            "time": "10:00 AM",
            "message": "Appointment Booked",
            "color": "primary",
        },
        {
            "time": "10:45 AM",
            "message": "Bill Generated",
            "color": "warning",
        },
        {
            "time": "11:30 AM",
            "message": "Medicine Issued",
            "color": "info",
        },
    ]

    context = {
        "total_patients": Patient.objects.count(),
        "total_appointments": Appointment.objects.count(),
        "total_bills": Billing.objects.count(),
        "total_medicines": Medicine.objects.count(),

        "today_appointments": Appointment.objects.order_by(
            "-appointment_date",
            "-appointment_time"
        )[:5],

        "recent_bills": Billing.objects.order_by("-id")[:5],

        "notifications": notifications,
        "activities": activities,
    }

    return render(
        request,
        "users/reception_dashboard.html",
        context,
    )

@login_required
def profile(request):

    user_profile = request.user.userprofile

    if request.method == "POST":

        form = UserProfileForm(
            request.POST,
            instance=user_profile
        )

        if form.is_valid():
            form.save()
            return redirect("profile")

    else:

        form = UserProfileForm(
            instance=user_profile
        )


    context = {
        "form": form,
        "user": request.user,
        "profile": user_profile,
    }

    return render(
        request,
        "users/profile.html",
        context
    )

@login_required
def change_password(request):

    if request.method == "POST":

        form = PasswordChangeForm(
            request.user,
            request.POST
        )

        if form.is_valid():

            user = form.save()

            update_session_auth_hash(
                request,
                user
            )

            messages.success(
                request,
                "Password changed successfully."
            )

            return redirect("profile")

    else:

        form = PasswordChangeForm(request.user)

    return render(
        request,
        "users/change_password.html",
        {
            "form": form
        }
    )