from django.forms import ModelForm
from django import forms

from .models import computer_inventory


class computer_inventoryForm(ModelForm):
    
    class Meta:
        model = computer_inventory
        fields = '__all__'