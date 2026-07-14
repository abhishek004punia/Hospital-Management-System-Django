from django.contrib.auth.decorators import login_required
from accounts.decorators import prescription_access_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Prescription
from .forms import PrescriptionForm

@login_required
@prescription_access_required
def add_prescription(request):

    if request.method == "POST":

        form = PrescriptionForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("prescription_list")

    else:
        form = PrescriptionForm()

    return render(request, "prescriptions/add_prescription.html", {
        "form": form
    })

@login_required
@prescription_access_required
def prescription_list(request):

    prescriptions = Prescription.objects.all().order_by("-id")

    return render(request, "prescriptions/prescription_list.html", {
        "prescriptions": prescriptions
    })

@login_required
@prescription_access_required
def prescription_detail(request, id):

    prescription = get_object_or_404(Prescription, id=id)

    return render(request, "prescriptions/prescription_detail.html", {
        "prescription": prescription
    })

@login_required
@prescription_access_required
def edit_prescription(request, id):

    prescription = get_object_or_404(Prescription, id=id)

    if request.method == "POST":

        form = PrescriptionForm(request.POST, instance=prescription)

        if form.is_valid():
            form.save()
            return redirect("prescription_list")

    else:
        form = PrescriptionForm(instance=prescription)

    return render(request, "prescriptions/edit_prescription.html", {
        "form": form
    })

@login_required
@prescription_access_required
def delete_prescription(request, id):

    prescription = get_object_or_404(Prescription, id=id)

    if request.method == "POST":
        prescription.delete()
        return redirect("prescription_list")

    return render(request, "prescriptions/delete_prescription.html", {
        "prescription": prescription
    })