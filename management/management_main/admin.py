from django.contrib import admin
from .models import *



admin.site.register(ProjectHours)



class EmployeesView(admin.ModelAdmin):
    list_display=('last_name', 'first_name', 'nickname', 'project')
    search_fields = ('last_name', 'first_name', 'nickname')
    list_filter =('project',)

admin.site.register(Employees, EmployeesView)
