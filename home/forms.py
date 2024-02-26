from django import forms
from home.models import Signup  # Adjust the import path according to your project structure


class SignupForm(forms.ModelForm):
    class Meta:
        model = Signup
        fields = ['name', 'email']
