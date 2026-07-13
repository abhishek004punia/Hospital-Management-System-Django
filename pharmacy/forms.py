from django import forms

from .models import Medicine


class MedicineForm(forms.ModelForm):

    class Meta:

        model = Medicine

        fields = "__all__"

        widgets = {

            "expiry_date": forms.DateInput(
                attrs={"type": "date"}
            ),

            "description": forms.Textarea(
                attrs={"rows": 3}
            ),

        }
        