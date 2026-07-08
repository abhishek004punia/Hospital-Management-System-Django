from django.shortcuts import render, redirect
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