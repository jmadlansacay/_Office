from django import forms
from hr.models import HrMaster


class HrMasterStyled(forms.ModelForm):
    class Meta:
        model = HrMaster
        fields =('employee_id', 'employee_type', 'last_name', 'first_name', 'middle_name', 'employee_status', 'gender' ,'project','civil_status')

        widgets = {
            'employee_id' : forms.TextInput(attrs={'class':'form-control'}),
            'employee_type' : forms.Select(attrs={'class':'form-control'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control'}),
            'first_name' : forms.TextInput(attrs={'class':'form-control'}),
            'middle_name' : forms.TextInput(attrs={'class':'form-control'}),
            'employee_status': forms.Select(attrs={'class':'form-control'}),
            'gender' : forms.Select(attrs={'class':'form-control'}),
            'project' : forms.Select(attrs={'class':'form-control'}),
            'civil_status' : forms.Select(attrs={'class':'form-control'}),

        }
