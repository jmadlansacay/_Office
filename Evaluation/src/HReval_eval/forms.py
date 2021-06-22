from django.forms import ModelForm
from django import forms
from django.utils.safestring import mark_safe


from  .models import HrMasterPayrollDetail, EmployeeEval


class HrMasterPayrollDetailForm(ModelForm):
    
    class Meta:
        model = HrMasterPayrollDetail
        fields = '__all__'


class EmployeeEvalForm(ModelForm):
    RATING = [
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
    ]
    cooperativeness = forms.ChoiceField(choices=RATING, widget=forms.RadioSelect(), required=True)
    time_panctuality = forms.ChoiceField(choices=RATING, widget=forms.RadioSelect(), required=True)
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


