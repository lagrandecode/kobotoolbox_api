from .models import *
from django import forms



class KoboForm(forms.ModelForm):
    class Meta:
        model = Kobo
        fields = ['name',]



class MyForm(forms.Form):
    name = forms.CharField(max_length=200)