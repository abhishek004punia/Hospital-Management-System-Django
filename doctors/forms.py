from django import forms
from .models import Doctor


class DoctorForm(forms.ModelForm):

    class Meta:
        model = Doctor

        fields = '__all__'

        widgets = {

            'doctor_id': forms.TextInput(attrs={'class': 'form-control'}),

            'full_name': forms.TextInput(attrs={'class': 'form-control'}),

            'specialization': forms.TextInput(attrs={'class': 'form-control'}),

            'qualification': forms.TextInput(attrs={'class': 'form-control'}),

            'experience': forms.NumberInput(attrs={'class': 'form-control'}),

            'mobile': forms.TextInput(attrs={'class': 'form-control'}),

            'email': forms.EmailInput(attrs={'class': 'form-control'}),

            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),

            'joining_date': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),
        }