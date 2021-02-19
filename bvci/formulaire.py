from django.forms import ModelForm
from django import forms
from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('nom_complet', 'email', 'numero', 'message')

        widget = {
            'nom_complet' : forms.TextInput(attrs={'class': 'form-control'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control'}),
            #'numero' : forms.IntegerInput(attrs={'class': 'form-control'}),
            'message' : forms.Textarea(attrs={'class': 'form-control'}),
        }