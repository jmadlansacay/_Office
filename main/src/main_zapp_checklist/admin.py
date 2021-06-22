from django.contrib import admin
from .models import *
# Register your models here.


class health_checklistView(admin.ModelAdmin):

    def employee_name(self,obj):
        return obj.employee.last_name + ', ' + obj.employee.first_name + ' ' +obj.employee.middle_name[:1] + '. (' + obj.employee.nick_name +')' 


    list_display = ('employee','employee_name', 'checklist_date', 'nature_of_visit','body_temp_check', 'sore_throat',
        'body_pain', 'head_ache', 'fever', 'question_two', 'question_three', 'question_four', 'question_five')

    search_fields=('employee__last_name','employee__first_name','employee__middle_name','employee__nick_name', 'checklist_date')


admin.site.register(health_checklist, health_checklistView)


