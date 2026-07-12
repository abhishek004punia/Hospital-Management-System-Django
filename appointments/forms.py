from django import forms
from .models import Appointment


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        
        exclude = [
            'appointment_id',
            'created_at',
            'updated_at',
        ]

        widgets = {

            'patient': forms.Select(
                attrs={'class': 'form-control'}
            ),

            'doctor': forms.Select(
                attrs={'class': 'form-control'}
            ),

            'appointment_date': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),

            'appointment_time': forms.TimeInput(
                attrs={
                    'class': 'form-control',
                    'type': 'time'
                }
            ),

            'status': forms.Select(
                attrs={'class': 'form-control'}
            ),

            'reason': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 3,
                    'placeholder' : 'Enter appointment reason'
                }
            ),
        }