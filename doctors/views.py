from django.shortcuts import render, redirect, get_object_or_404
from .models import Doctor
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

def doctor_list(request):

    doctors = Doctor.objects.all()

    return render(request, 'doctors/doctor_list.html', {
        'doctors': doctors
    })

def doctor_detail(request, id):

    doctor = get_object_or_404(Doctor, id=id)

    return render(request, 'doctors/doctor_detail.html', {
        'doctor': doctor
    })

def edit_doctor(request, id):

    doctor = get_object_or_404(Doctor, id=id)

    if request.method == "POST":

        form = DoctorForm(request.POST, instance=doctor)

        if form.is_valid():
            form.save()
            return redirect('doctor_list')

    else:

        form = DoctorForm(instance=doctor)

    return render(request, 'doctors/edit_doctor.html', {
        'form': form
    })

def delete_doctor(request, id):

    doctor = get_object_or_404(Doctor, id=id)

    if request.method == "POST":

        doctor.delete()

        return redirect('doctor_list')

    return render(request, 'doctors/delete_doctor.html', {
        'doctor': doctor
    })