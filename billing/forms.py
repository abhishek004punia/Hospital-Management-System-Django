from django import forms
from .models import Billing


class BillingForm(forms.ModelForm):

    class Meta:
        model = Billing

        exclude = [
            'bill_id',
            'doctor',
            'patient',
            'consultation_fee',
            'total_amount',
            'created_at',
            'updated_at',
        ]

        widgets = {

            'appointment': forms.Select(
                attrs={'class': 'form-control'}
            ),

            'medicine_charge': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'step': '0.01'
                }
            ),

            'test_charge': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'step': '0.01'
                }
            ),

            'other_charge': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'step': '0.01'
                }
            ),

            'payment_status': forms.Select(
                attrs={'class': 'form-control'}
            ),

            'bill_date': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),
        }