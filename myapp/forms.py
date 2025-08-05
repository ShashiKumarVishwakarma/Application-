from django import forms
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    user_type = forms.ChoiceField(choices=[('Patient', 'Patient'), ('Doctor', 'Doctor')])
    profile_picture = forms.ImageField(required=False)
    address_line1 = forms.CharField()
    city = forms.CharField()
    state = forms.CharField()
    pincode = forms.CharField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'confirm_password',
                  'user_type', 'profile_picture', 'address_line1', 'city', 'state', 'pincode']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
