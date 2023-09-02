from .models import *
from django import forms



class KoboForm(forms.ModelForm):
    class Meta:
        model = Kobo
        fields = ['name',]