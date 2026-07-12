from django import forms
from .models import Doctor


class DoctorForm(forms.ModelForm):

    class Meta:
        model = Doctor
        fields = "__all__"

        widgets = {
            "full_name": forms.TextInput(attrs={"class": "form-control"}),
            "specialization": forms.TextInput(attrs={"class": "form-control"}),
            "department": forms.TextInput(attrs={"class": "form-control"}),

            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "mobile": forms.TextInput(attrs={"class": "form-control"}),

            "gender": forms.Select(attrs={"class": "form-select"}),

            "qualification": forms.TextInput(attrs={"class": "form-control"}),

            "experience": forms.NumberInput(attrs={"class": "form-control"}),

            "consultation_fee": forms.NumberInput(attrs={"class": "form-control"}),

            "available_from": forms.TimeInput(
                attrs={
                    "class": "form-control",
                    "type": "time"
                }
            ),

            "available_to": forms.TimeInput(
                attrs={
                    "class": "form-control",
                    "type": "time"
                }
            ),

            "address": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3
                }
            ),

            "status": forms.Select(attrs={"class": "form-select"}),
        }