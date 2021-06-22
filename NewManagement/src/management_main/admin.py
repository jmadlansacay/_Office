from django.contrib import admin
from .models import *



class ProjectHoursView(admin.ModelAdmin):
    list_display=('project', 'year', 'jan_hrs', 'feb_hrs', 'mar_hrs', 'apr_hrs', 'may_hrs', 'jun_hrs', 'jul_hrs', 'aug_hrs', 'sep_hrs', 'oct_hrs', 'nov_hrs', 'dec_hrs')
    search_fields = ('project', 'year')
    list_filter = ('year', 'project', )


admin.site.register(ProjectHours, ProjectHoursView)


class EmployeesView(admin.ModelAdmin):
    list_display=('last_name', 'first_name', 'nickname', 'project', 'project_type', 'nationality', 'employee_status', 'employee_type', 'remarks')
    search_fields = ('last_name', 'first_name', 'nickname')
    list_filter =('nationality', 'project_type', 'employee_status', 'employee_type', 'project',)


admin.site.register(Employees, EmployeesView)

class EmployeeHoursView(admin.ModelAdmin):
    list_display = ('employee', 'year', 'jan_hrs', 'feb_hrs', 'mar_hrs', 'apr_hrs', 'may_hrs', 'jun_hrs', 'jul_hrs', 'aug_hrs', 'sep_hrs', 'oct_hrs', 'nov_hrs', 'dec_hrs')
    search_fields = ('employee', 'year')
    list_filter = ('year', 'employee')

admin.site.register(EmployeeHours, EmployeeHoursView)

admin.site.register(HeadCount)

admin.site.register(Covid)

admin.site.register(Events)

admin.site.register(Financial)

admin.site.register(Managers)