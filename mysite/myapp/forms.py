from django import forms
from django.contrib.auth.forms import UserCreationForm, UserLoginForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True , label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        label = {'email':'Email'}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'})}
