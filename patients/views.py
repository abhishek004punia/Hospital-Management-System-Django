from django.shortcuts import render, redirect, get_object_or_404
from .forms import PatientForm
from .models import Patient


def add_patient(request):

    if request.method == "POST":
        form = PatientForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('add_patient')

    else:
        form = PatientForm()

    return render(request, 'patients/add_patient.html', {
        'form': form
    })


def patient_list(request):

    search = request.GET.get('search')

    if search:
        patients = Patient.objects.filter(
            full_name__icontains=search
        )
    else:
        patients = Patient.objects.all()


    return render(request, 'patients/patient_list.html', {
        'patients': patients
    })

def patient_detail(request, id):

    patient = get_object_or_404(Patient, id=id)

    return render(request, 'patients/patient_detail.html', {
        'patient': patient
    })