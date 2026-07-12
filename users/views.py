from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages



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

def doctor_dashboard(request):

    return render(
        request,
        "users/doctor_dashboard.html"
    )


def reception_dashboard(request):

    return render(
        request,
        "users/reception_dashboard.html"
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