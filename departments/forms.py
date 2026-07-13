from django import forms
from .models import Department


class DepartmentForm(forms.ModelForm):

    class Meta:
        model = Department

        fields = [
            "department_name",
            "department_head",
            "location",
            "description",
        ]

        widgets = {

            "department_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Department Name"
            }),

            "department_head": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Department Head"
            }),

            "location": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Department Location"
            }),

            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Enter Description"
            }),

        }