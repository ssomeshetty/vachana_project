from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "email", "password1", "password2", "date_of_birth"]

    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),  # This will give a date picker in the form
    )

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "email", "date_of_birth", "is_staff", "is_active"]
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),  # This will give a date picker in the form
    )

class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email','picture','phone_number']

