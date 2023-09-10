from .models import *
from django import forms



class KoboForm(forms.ModelForm):
    class Meta:
        model = Kobo
        fields = ['name',]



class MyForm(forms.Form):
    name = forms.CharField(max_length=200)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'



class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'