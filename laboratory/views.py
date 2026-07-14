from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from .models import LabTest
from .forms import LabTestForm
from django.contrib.auth.decorators import login_required
from accounts.decorators import laboratory_access_required


# Add Lab Test
@login_required
@laboratory_access_required
def add_lab_test(request):

    if request.method == "POST":

        form = LabTestForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("lab_test_list")

    else:

        form = LabTestForm()

    return render(
        request,
        "laboratory/add_lab_test.html",
        {
            "form": form
        }
    )


# Lab Test List
@login_required
@laboratory_access_required
def lab_test_list(request):

    query = request.GET.get("q")

    tests = LabTest.objects.all()

    if query:

        tests = tests.filter(
            Q(patient_name__icontains=query) |
            Q(doctor_name__icontains=query) |
            Q(test_name__icontains=query)
        )

    return render(
        request,
        "laboratory/lab_test_list.html",
        {
            "tests": tests,
            "query": query,
        }
    )


# Lab Test Detail
@login_required
@laboratory_access_required
def lab_test_detail(request, id):

    test = get_object_or_404(
        LabTest,
        test_id=id
    )

    return render(
        request,
        "laboratory/lab_test_detail.html",
        {
            "test": test
        }
    )


# Edit Lab Test
@login_required
@laboratory_access_required
def edit_lab_test(request, id):

    test = get_object_or_404(
        LabTest,
        test_id=id
    )

    if request.method == "POST":

        form = LabTestForm(
            request.POST,
            instance=test
        )

        if form.is_valid():

            form.save()

            return redirect("lab_test_list")

    else:

        form = LabTestForm(
            instance=test
        )

    return render(
        request,
        "laboratory/edit_lab_test.html",
        {
            "form": form
        }
    )


# Delete Lab Test
@login_required
@laboratory_access_required
def delete_lab_test(request, id):

    test = get_object_or_404(
        LabTest,
        test_id=id
    )

    if request.method == "POST":

        test.delete()

        return redirect("lab_test_list")

    return render(
        request,
        "laboratory/delete_lab_test.html",
        {
            "test": test
        }
    )