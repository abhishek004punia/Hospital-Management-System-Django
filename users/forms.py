from django import forms
from .models import UserProfile


class LoginForm(forms.Form):

    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Username",
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Password",
            }
        )
    )

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile

        fields = [
            "mobile",
            "address",
        ]

        widgets = {
            "mobile": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter mobile number"
                }
            ),

            "address": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter address",
                    "rows": 4
                }
            ),
        }    