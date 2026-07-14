from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from .models import Department
from .forms import DepartmentForm
from django.contrib.auth.decorators import login_required
from accounts.decorators import admin_required


# Add Department
@login_required
@admin_required
def add_department(request):

    if request.method == "POST":

        form = DepartmentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("department_list")

    else:
        form = DepartmentForm()

    return render(
        request,
        "departments/add_department.html",
        {"form": form},
    )


# Department List
@login_required
@admin_required
def department_list(request):

    query = request.GET.get("q")

    departments = Department.objects.all()

    if query:

        departments = departments.filter(
            Q(department_name__icontains=query) |
            Q(department_head__icontains=query) |
            Q(location__icontains=query)
        )

    context = {
        "departments": departments,
        "query": query,
    }

    return render(
        request,
        "departments/department_list.html",
        context,
    )


# Department Detail
@login_required
@admin_required
def department_detail(request, id):

    department = get_object_or_404(
        Department,
        department_id=id,
    )

    return render(
        request,
        "departments/department_detail.html",
        {
            "department": department
        },
    )


# Edit Department
@login_required
@admin_required
def edit_department(request, id):

    department = get_object_or_404(
        Department,
        department_id=id,
    )

    if request.method == "POST":

        form = DepartmentForm(
            request.POST,
            instance=department,
        )

        if form.is_valid():
            form.save()
            return redirect("department_list")

    else:

        form = DepartmentForm(
            instance=department
        )

    return render(
        request,
        "departments/edit_department.html",
        {
            "form": form,
        },
    )


# Delete Department
@login_required
@admin_required
def delete_department(request, id):

    department = get_object_or_404(
        Department,
        department_id=id,
    )

    if request.method == "POST":

        department.delete()

        return redirect("department_list")

    return render(
        request,
        "departments/delete_department.html",
        {
            "department": department,
        },
    )