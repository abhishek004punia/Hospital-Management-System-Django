from django.shortcuts import render, redirect, get_object_or_404
from .forms import BillingForm
from .models import Billing


def add_bill(request):

    if request.method == "POST":

        form = BillingForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("bill_list")

    else:

        form = BillingForm()

    return render(
        request,
        "billing/add_bill.html",
        {
            "form": form
        }
    )


def bill_list(request):

    bills = Billing.objects.all()

    return render(
        request,
        "billing/bill_list.html",
        {
            "bills": bills
        }
    )
def bill_detail(request, id):

    bill = get_object_or_404(
        Billing,
        id=id
    )

    return render(
        request,
        "billing/bill_detail.html",
        {
            "bill": bill
        }
    )

def edit_bill(request, id):

    bill = get_object_or_404(Billing, id=id)

    if request.method == "POST":

        form = BillingForm(request.POST, instance=bill)

        if form.is_valid():

            form.save()

            return redirect("bill_list")

    else:

        form = BillingForm(instance=bill)

    return render(
        request,
        "billing/edit_bill.html",
        {
            "form": form
        }
    )

def delete_bill(request, id):

    bill = get_object_or_404(Billing, id=id)

    if request.method == "POST":

        bill.delete()

        return redirect("bill_list")

    return render(
        request,
        "billing/delete_bill.html",
        {
            "bill": bill
        }
    )