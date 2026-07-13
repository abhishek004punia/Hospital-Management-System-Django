from django import forms

from .models import LabTest


class LabTestForm(forms.ModelForm):

    class Meta:

        model = LabTest

        fields = "__all__"

        widgets = {

            "test_date": forms.DateInput(
                attrs={"type": "date"}
            ),

            "remarks": forms.Textarea(
                attrs={"rows": 3}
            ),

        }