from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Category)
admin.site.register(SubCategory)

class EvaluationCriteriaView(admin.ModelAdmin):

    def category(self,obj):
        return obj.sub_category.category

    def sub_category(self,obj):
        return obj.sub_category      

    list_display = ('sub_category', 'description', 'group')
    list_filter = ['sub_category__category__name','group']

admin.site.register(EvaluationCriteria, EvaluationCriteriaView)



class EmployeeTreeView(admin.ModelAdmin):

    def project(self,obj):
        return obj.employee.project_code

    list_display = ('employee', 'access','skill_set', 'project_area', 'project')
    list_filter =('skill_set',)


admin.site.register(EmployeeTree,EmployeeTreeView)




class EvaluationView(admin.ModelAdmin):
    
    list_display=('employee', 'criteria', 'area_lead', 'project_lead', 'manager')
    list_filter=('employee',)


admin.site.register(Evaluation,EvaluationView)


admin.site.register(comandsugg)