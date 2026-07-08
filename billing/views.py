from django.shortcuts import render, redirect
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