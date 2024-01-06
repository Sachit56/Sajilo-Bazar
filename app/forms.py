from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm,PasswordResetForm
from django.contrib.auth import password_validation

class RegistrationForm(UserCreationForm):
    username=forms.CharField(label='Username',max_length=100,widget=forms.TextInput({'class':'form-control'}))
    email=forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Repeat Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model=User

        fields=['username','email','password1','password2']

class LoginForm(AuthenticationForm):
    username=forms.CharField(label='Username', max_length=100,widget=forms.TextInput({'autofocus':True,'class':'form-control'}))
    password=forms.CharField(label='Password',max_length=100,widget=forms.PasswordInput({'autocomplete':'current-password','class':'form-control'}))

class PasswordChangeForm(PasswordChangeForm):
    old_password=forms.CharField(label='Old Password',strip=False,max_length=100,widget=forms.PasswordInput({'autocomplete':'current-password','class':'form-control'}))
    new_password1=forms.CharField(label='New Password',help_text=password_validation,max_length=100,widget=forms.PasswordInput({'autocomplete':'current-password','class':'form-control'}))
    new_password2=forms.CharField(label='Repeat New Password',max_length=100,widget=forms.PasswordInput({'autocomplete':'current-password','class':'form-control'}))

class PasswordResetForm(PasswordResetForm):
    email=forms.EmailField(label='Email',max_length=200,widget=forms.EmailInput(attrs={'autofocus':True,'class':'form-control'}))

