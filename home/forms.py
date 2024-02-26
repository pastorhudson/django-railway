from django import forms
from .models import Signup  # Adjust the import path according to your project structure


class SignupForm(forms.ModelForm):
    class Meta:
        model = Signup
        fields = ['email', 'name']

    # Optionally, you can customize the form fields here
    # For example, to use a PasswordInput widget for the password field:
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput()
