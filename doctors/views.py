from django.shortcuts import render, redirect
from .forms import DoctorForm


def add_doctor(request):

    if request.method == "POST":

        form = DoctorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('add_doctor')

    else:

        form = DoctorForm()

    return render(request, 'doctors/add_doctor.html', {
        'form': form
    })