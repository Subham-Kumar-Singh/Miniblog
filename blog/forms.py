from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class Signupform(UserCreationForm):
    password2=forms.CharField(label="Confim Password (again)")
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels={'email':"Email "}
