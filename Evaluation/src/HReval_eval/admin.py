from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(EmployeeEval)


class HrMasterView(admin.ModelAdmin):
    list_display =('employee_type', 'employee_id','employee_status','last_name','first_name', 'nickname','gender')
    list_filter=['employee_type','gender','employee_status']
    search_fields = ('employee_id', 'last_name','first_name', 'nickname')
    
admin.site.register(HrMaster, HrMasterView)


class HrMasterWorkDetailView(admin.ModelAdmin):
    def employee_name(self,obj):
        return obj.empl.last_name + ', ' + obj.empl.first_name + ' ' + obj.empl.middle_name +' (' + obj.empl.nickname +') '

    list_display=('employee_name', 'sss_no','tin','philhealth_no','pagibig_no',)  
    search_fields=('empl__last_name','empl__first_name','empl__middle_name','empl__nickname')

admin.site.register(HrMasterWorkDetail,HrMasterWorkDetailView)


class HrMasterAddressView(admin.ModelAdmin):
    def employee_name(self,obj):
        return obj.empl_address.last_name + ', ' + obj.empl_address.first_name + ' ' + obj.empl_address.middle_name +' (' + obj.empl_address.nickname +') '

    list_display  = ('employee_name', 'permanent_town', 'permanent_province')
    search_fields=('empl_address__last_name','empl_address__first_name','empl_address__middle_name','empl_address__nickname')
    list_filter=['permanent_province',]

admin.site.register(HrMasterAddress, HrMasterAddressView)


class HrMasterPayrollDetailView(admin.ModelAdmin):
    def employee_name(self,obj):
        return obj.empl_payroll.last_name + ', ' + obj.empl_payroll.first_name + ' ' + obj.empl_payroll.middle_name +' (' + obj.empl_payroll.nickname +') '

    list_display  = ('employee_name', )
    search_fields=('empl_payroll__last_name','empl_payroll__first_name','empl_payroll__middle_name','empl_payroll__nickname')
    
admin.site.register(HrMasterPayrollDetail, HrMasterPayrollDetailView)



admin.site.register(EmployeeTypeCode)
admin.site.register(EmployeeStatusCode)

class UserDetailView(admin.ModelAdmin):
    list_display =('user','last_name','first_name','permission')
    autocomplete_fields = ['user']

    def last_name(self,obj):
        return obj.user.last_name
    
    def first_name(self,obj):
        return obj.user.first_name


admin.site.register(UserDetail,UserDetailView)


class ProjectCodeView(admin.ModelAdmin):
    list_display = ('description' ,'project_name','start_date', 'end_date')
    list_filter = ('project_supervisor',)


admin.site.register(ProjectCode, ProjectCodeView)
admin.site.register(DesignationCode)



