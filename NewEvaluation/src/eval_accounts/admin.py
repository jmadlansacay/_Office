from django.contrib import admin
from .models import *
from eval_main.models import MainHrHrMaster
# Register your models here.

class AccountDetailsView(admin.ModelAdmin):
    list_display = ('mhi_id', 'last_name', 'first_name', 'nick_name','access','pic','employee_id','project', 'area', 'skill_set')
    search_fields = ('mhi_id', 'last_name', 'first_name', 'nick_name',)
    list_filter = ('access','project','skill_set','area')

admin.site.register(AccountDetails, AccountDetailsView)
admin.site.register(UserAccess)
admin.site.register(EvaluationPeriod)



