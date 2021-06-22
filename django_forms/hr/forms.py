from django.forms import ModelForm
from .models import HrMaster


class HrMasterForm(ModelForm):
    class Meta:
        model = HrMaster
        fields = '__all__'