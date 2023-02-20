from django import forms
from .models import *


class AddNewOrder(forms.ModelForm):

    class Meta:
        model = NewOrder
        fields = "__all__"

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-c'}),
            'last_name': forms.TextInput(attrs={'class': 'form-c'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-c'}),
            'telephone_number': forms.TextInput(attrs={'class': 'form-c'}),
            'email': forms.TextInput(attrs={'class': 'form-c'}),
            'link_messenger': forms.TextInput(attrs={'class': 'form-c'}),
            'info_order': forms.Textarea(attrs={'class': 'input-text-area'}),
            'car_brand': forms.TextInput(attrs={'class': 'form-c'}),
            'car_model': forms.TextInput(attrs={'class': 'form-c'}),
            'car_year': forms.TextInput(attrs={'class': 'form-c'}),
            'car_horsepower': forms.TextInput(attrs={'class': 'form-c'}),
            'car_vin': forms.TextInput(attrs={'class': 'form-c'})
        }
