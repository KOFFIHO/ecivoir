from django.forms import ModelForm, TextInput, EmailInput,Textarea
from django.forms import ModelForm,Form
from django import forms
from .models import Contact

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']
        


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['nom_complet','email','message','numero']
        widgets = {
            'nom_complet': TextInput(attrs={'placeholder':'Quel est votre nom ?','class':'form-control'}),
            'email': EmailInput(attrs={'placeholder':' Entrez votre email','class':'form-control'}),
            'numero': TextInput(attrs={'placeholder':'+ 225 34265498','class':'form-control'}),
            'message': Textarea(attrs={'placeholder':'Quelle est votre préocupation ?','class':'form-control'}),
        }