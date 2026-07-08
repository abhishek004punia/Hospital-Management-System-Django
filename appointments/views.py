from django.shortcuts import render, redirect
from .forms import AppointmentForm


def add_appointment(request):

    if request.method == "POST":

        form = AppointmentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('add_appointment')

    else:

        form = AppointmentForm()

    return render(request, 'appointments/add_appointment.html', {
        'form': form
    })