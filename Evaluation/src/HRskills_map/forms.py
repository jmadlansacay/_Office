from django.forms import ModelForm
from django import forms
from django.utils.safestring import mark_safe

from .models import *

class EvaluationForm(ModelForm):
    RATING = [
        ('#' , '#'),
        ('0' , '0'),
        ('1' , '1'),
        ('2' , '2'),
        ('3' , '3'),
        ('4' , '4'),
    ]

    self_rating = forms.ChoiceField(choices=RATING, widget=forms.RadioSelect(), required=True)
    area_lead_rating = forms.ChoiceField(choices=RATING, widget=forms.RadioSelect(), required=True)
    project_lead_rating = forms.ChoiceField(choices=RATING, widget=forms.RadioSelect(), required=True)
    manager_rating = forms.ChoiceField(choices=RATING, widget=forms.RadioSelect(), required=True)

    class Meta:
        fields = ['criteria','self_rating', 'area_lead_rating','project_lead_rating', 'manager_rating','actions']





class comandsuggForm(ModelForm):
    
    class Meta:
        model = comandsugg
        fields = '__all__'