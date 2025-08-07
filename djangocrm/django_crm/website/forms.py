from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email", widget=forms.TelInput(attrs={'class': 'form-control', }))
    first_name = forms.CharField(label="First Name", max_length=100, widget=forms.TelInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label="Last Name",
                                max_length=100, widget=forms.TelInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ('Username', 'first_name', 'last_name', 'email', 'password1', 'password2')