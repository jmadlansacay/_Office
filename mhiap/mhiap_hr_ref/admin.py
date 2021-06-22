from django.contrib import admin
from .models import EmployeeTypeCode, UserDetail, EmployeeStatusCode, ProjectCode, DesignationCode
# Register your models here.

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

