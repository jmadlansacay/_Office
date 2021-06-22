from django.forms import ModelForm
from .models import HrMaster, HrMasterWorkDetail, HrMasterAddress, HrMasterPayrollDetail
from django import forms
from django.utils.safestring import mark_safe


class HrMasterModelForm(ModelForm):

    class Meta:
        model = HrMaster
        fields = '__all__'


class HrMasterWorkDetailForm(ModelForm):

    class Meta: 
        model = HrMasterWorkDetail
        fields = '__all__'


class HrMasterAddressForm(ModelForm):

    class Meta: 
        model = HrMasterAddress
        fields = '__all__'


class HrMasterPayrollDetailForm(ModelForm):

    class Meta:
        model = HrMasterPayrollDetail
        fields = '__all__'
        