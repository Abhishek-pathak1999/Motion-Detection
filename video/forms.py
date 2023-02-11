from dataclasses import fields
from pyexpat import model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms

class SignupForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
        'class':'input ',
        'placeholder':'Username',
        'autocomplete':"off"
        }
    ))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
        'class':'input ',
        'placeholder':'Email',
        'autocomplete':"off"
        }
    ))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
        'class':'input ',
        'placeholder':'Password',
        'autocomplete':"off"
        }
    ))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
        'class':'input ',
        'placeholder':'Confirm Password',
        'autocomplete':"off"
        }
    ))
    
    class Meta:
        model=User
        fields=['username','email']

#Signup view 
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
        'class':'input ',
        'placeholder':'Email',
        'autocomplete':"off",
        }
    ))
   
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
        'class':'input ',
        'placeholder':'Confirm Password',
        'autocomplete':"off"
        }
    ))
    

    



 
