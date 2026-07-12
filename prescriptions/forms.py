from django import forms
from .models import Prescription


class PrescriptionForm(forms.ModelForm):

    class Meta:
        model = Prescription

        fields = [
            'appointment',
            'patient',
            'doctor',
            'medicine',
            'dosage',
            'duration',
            'instructions',
            'status',
        ]

        widgets = {

            'appointment': forms.Select(
                attrs={'class': 'form-control'}
            ),

            'patient': forms.Select(
                attrs={'class': 'form-control'}
            ),

            'doctor': forms.Select(
                attrs={'class': 'form-control'}
            ),

            'medicine': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'dosage': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'duration': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'instructions': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 3
                }
            ),

            'status': forms.Select(
                attrs={'class': 'form-control'}
            ),
        }