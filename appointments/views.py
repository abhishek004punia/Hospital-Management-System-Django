from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .forms import AppointmentForm
from .models import Appointment
from django.contrib.auth.decorators import login_required
from accounts.decorators import appointment_access_required

@login_required
@appointment_access_required
def add_appointment(request):

    if request.method == "POST":

        form = AppointmentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('appointment_list')

    else:

        form = AppointmentForm()

    return render(request, 'appointments/add_appointment.html', {
        'form': form
    })

@login_required
@appointment_access_required
def appointment_list(request):

    query = request.GET.get("q")

    appointments = Appointment.objects.select_related(
        "patient",
        "doctor"
    )

    if query:

        appointments = appointments.filter(

            Q(patient__full_name__icontains=query) |

            Q(doctor__full_name__icontains=query) |

            Q(status__icontains=query)

        )

    return render(
        request,
        "appointments/appointment_list.html",
        {
            "appointments": appointments,
            "query": query,
        }
    )

@login_required
@appointment_access_required
def appointment_detail(request, id):

    appointment = get_object_or_404(
        Appointment,
        id=id
    )

    return render(
        request,
        'appointments/appointment_detail.html',
        {
            'appointment': appointment
        }
    )

@login_required
@appointment_access_required
def edit_appointment(request, id):

    appointment = get_object_or_404(
        Appointment,
        id=id
    )

    if request.method == "POST":

        form = AppointmentForm(
            request.POST,
            instance=appointment
        )

        if form.is_valid():
            form.save()
            return redirect('appointment_list')

    else:

        form = AppointmentForm(
            instance=appointment
        )

    return render(
        request,
        'appointments/edit_appointment.html',
        {
            'form': form
        }
    )

@login_required
@appointment_access_required
def delete_appointment(request, id):

    appointment = get_object_or_404(
        Appointment,
        id=id
    )

    if request.method == "POST":

        appointment.delete()

        return redirect("appointment_list")

    return render(
        request,
        "appointments/delete_appointment.html",
        {
            "appointment": appointment
        }
    )