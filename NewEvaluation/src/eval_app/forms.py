from django.forms import ModelForm
from django import forms

from .models import EmployeeEval, Comments



class EmployeeEvalForm(ModelForm):
    RATING = [
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
    ]
    cooperativeness = forms.ChoiceField(choices=RATING, widget=forms.RadioSelect(), required=True,)
    time_panctuality = forms.ChoiceField(choices=RATING, widget=forms.RadioSelect(), required=False)
    costsaving= forms.ChoiceField(choices=RATING, widget=forms.RadioSelect(), required=True)
    speed= forms.ChoiceField(choices=RATING, widget=forms.RadioSelect(), required=True)
    accqlty= forms.ChoiceField(choices=RATING, widget=forms.RadioSelect(), required=True)
    workeff= forms.ChoiceField(choices=RATING, widget=forms.RadioSelect(), required=True)
    pdacycle= forms.ChoiceField(choices=RATING, widget=forms.RadioSelect(), required=True)
    loyalty= forms.ChoiceField(choices=RATING, widget=forms.RadioSelect(), required=True)
    team_player= forms.ChoiceField(choices=RATING, widget=forms.RadioSelect(), required=True)
    harmony= forms.ChoiceField(choices=RATING, widget=forms.RadioSelect(), required=True)

  

    class Meta:
        model = EmployeeEval
        fields = '__all__'


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

    self_rating = forms.ChoiceField(choices=RATING, required=True)
    area_lead_rating = forms.ChoiceField(choices=RATING, required=True)
    project_lead_rating = forms.ChoiceField(choices=RATING, required=True)
    manager_rating = forms.ChoiceField(choices=RATING, required=True)

    class Meta:
        fields = ['criteria','self_rating', 'area_lead_rating','project_lead_rating', 'manager_rating','actions']



class CommentsForm(ModelForm):


    RATING = [
        
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
    ]

    SHARING = [
        
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5 Do not want to answer'),
    ]
    
    dispatch_japan = forms.ChoiceField(choices=RATING, widget=forms.RadioSelect(), required=True)
    dispatch_singapore = forms.ChoiceField(choices=RATING, widget=forms.RadioSelect(), required=True)
    dispatch_philippines = forms.ChoiceField(choices=RATING, widget=forms.RadioSelect(), required=True)
    dispatch_us_canada = forms.ChoiceField(choices=RATING, widget=forms.RadioSelect(), required=True)
    dispatch_north_europe = forms.ChoiceField(choices=RATING, widget=forms.RadioSelect(), required=True)
    dispatch_bangladesh = forms.ChoiceField(choices=RATING, widget=forms.RadioSelect(), required=True)
    dispatch_russia = forms.ChoiceField(choices=RATING, widget=forms.RadioSelect(), required=True)
    dispatch_africa = forms.ChoiceField(choices=RATING, widget=forms.RadioSelect(), required=True)
    fairness_for_all = forms.ChoiceField(choices=RATING, widget=forms.RadioSelect(), required=True)
    terms_of_salary = forms.ChoiceField(choices=RATING, widget=forms.RadioSelect(), required=True)
    # rule_on_the_company = forms.ChoiceField(choices=RATING, widget=forms.RadioSelect(), required=True)
    # violation_action = forms.ChoiceField(choices=RATING, widget=forms.RadioSelect(), required=True)
    share_knowledge = forms.ChoiceField(choices=SHARING, widget=forms.RadioSelect(), required=True)
    think_yourself = forms.ChoiceField(choices=RATING, widget=forms.RadioSelect(), required=True)
   


    class Meta:
        model = Comments
        fields = '__all__'

