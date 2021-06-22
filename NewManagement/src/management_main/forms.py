from django.forms import ModelForm
from django import forms

from .models import *

class CovidForm(ModelForm):

    class Meta:
        model = Covid
        fields = '__all__'