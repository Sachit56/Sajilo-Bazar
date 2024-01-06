from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Registration(UserCreationForm):
    username=forms.CharField(label='Username',max_length=100,widget=forms.TextInput({'class':'form-control'}))
    email=forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Repeat Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model=User

        fields='__all__'