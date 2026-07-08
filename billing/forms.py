from django import forms
from .models import Billing


class BillingForm(forms.ModelForm):

    class Meta:

        model = Billing

        fields = "__all__"

        widgets = {

            "bill_id": forms.TextInput(attrs={"class": "form-control"}),

            "patient": forms.Select(attrs={"class": "form-select"}),

            "doctor": forms.Select(attrs={"class": "form-select"}),

            "appointment": forms.Select(attrs={"class": "form-select"}),

            "consultation_fee": forms.NumberInput(attrs={"class": "form-control"}),

            "medicine_charge": forms.NumberInput(attrs={"class": "form-control"}),

            "test_charge": forms.NumberInput(attrs={"class": "form-control"}),

            "other_charge": forms.NumberInput(attrs={"class": "form-control"}),

            "total_amount": forms.NumberInput(attrs={"class": "form-control"}),

            "payment_status": forms.Select(attrs={"class": "form-select"}),

            "bill_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date"
                }
            ),

        }