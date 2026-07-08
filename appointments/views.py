from django.shortcuts import render, redirect, get_object_or_404
from .forms import AppointmentForm
from .models import Appointment


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

def appointment_list(request):

    appointments = Appointment.objects.select_related(
        'patient',
        'doctor'
    ).all()

    return render(
        request,
        'appointments/appointment_list.html',
        {
            'appointments': appointments
        }
    )

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