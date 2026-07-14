from django.shortcuts import render, redirect, get_object_or_404
from .models import Billing
from .forms import BillingForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from accounts.decorators import billing_access_required

@login_required
@billing_access_required
def add_bill(request):

    if request.method == "POST":
        form = BillingForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('bill_list')

    else:
        form = BillingForm()

    return render(request, 'billing/add_bill.html', {
        'form': form
    })

@login_required
@billing_access_required
def bill_list(request):

    query = request.GET.get("q")

    bills = Billing.objects.all()

    if query:
        bills = bills.filter(
            Q(bill_id__icontains=query) |
            Q(patient__full_name__icontains=query) |
            Q(doctor__full_name__icontains=query)
        )

    return render(
        request,
        "billing/bill_list.html",
        {
            "bills": bills,
            "query": query,
        }
    )

@login_required
@billing_access_required
def bill_detail(request, id):

    bill = get_object_or_404(Billing, id=id)

    return render(request, 'billing/bill_detail.html', {
        'bill': bill
    })

@login_required
@billing_access_required
def edit_bill(request, id):

    bill = get_object_or_404(Billing, id=id)

    if request.method == "POST":

        form = BillingForm(request.POST, instance=bill)

        if form.is_valid():
            form.save()
            return redirect('bill_list')

    else:
        form = BillingForm(instance=bill)

    return render(request, 'billing/edit_bill.html', {
        'form': form,
        'bill': bill
    })

@login_required
@billing_access_required
def delete_bill(request, id):

    bill = get_object_or_404(Billing, id=id)

    if request.method == "POST":
        bill.delete()
        return redirect('bill_list')

    return render(request, 'billing/delete_bill.html', {
        'bill': bill
    })

@login_required
@billing_access_required
def print_bill(request, id):
    bill = get_object_or_404(Billing, id=id)
    return render(request, "billing/print_bill.html", {
        "bill": bill
    })