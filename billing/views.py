from django.shortcuts import render
from .forms import BillingForm


def add_bill(request):

    form = BillingForm()

    return render(
        request,
        "billing/add_bill.html",
        {
            "form": form
        }
    )