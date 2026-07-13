from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from .models import Medicine
from .forms import MedicineForm


# Add Medicine
def add_medicine(request):

    if request.method == "POST":

        form = MedicineForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("medicine_list")

    else:

        form = MedicineForm()

    return render(
        request,
        "pharmacy/add_medicine.html",
        {
            "form": form,
        }
    )


# Medicine List
def medicine_list(request):

    query = request.GET.get("q")

    medicines = Medicine.objects.all()

    if query:

        medicines = medicines.filter(
            Q(medicine_name__icontains=query) |
            Q(manufacturer__icontains=query) |
            Q(category__icontains=query)
        )

    return render(
        request,
        "pharmacy/medicine_list.html",
        {
            "medicines": medicines,
            "query": query,
        }
    )


# Medicine Detail
def medicine_detail(request, id):

    medicine = get_object_or_404(
        Medicine,
        medicine_id=id
    )

    return render(
        request,
        "pharmacy/medicine_detail.html",
        {
            "medicine": medicine
        }
    )


# Edit Medicine
def edit_medicine(request, id):

    medicine = get_object_or_404(
        Medicine,
        medicine_id=id
    )

    if request.method == "POST":

        form = MedicineForm(
            request.POST,
            instance=medicine
        )

        if form.is_valid():

            form.save()

            return redirect("medicine_list")

    else:

        form = MedicineForm(
            instance=medicine
        )

    return render(
        request,
        "pharmacy/edit_medicine.html",
        {
            "form": form
        }
    )


# Delete Medicine
def delete_medicine(request, id):

    medicine = get_object_or_404(
        Medicine,
        medicine_id=id
    )

    if request.method == "POST":

        medicine.delete()

        return redirect("medicine_list")

    return render(
        request,
        "pharmacy/delete_medicine.html",
        {
            "medicine": medicine
        }
    )

