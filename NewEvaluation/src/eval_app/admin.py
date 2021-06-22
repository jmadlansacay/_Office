from django.contrib import admin
from .models import EmployeeEval, Category, SubCategory, EvaluationCriteria, Evaluation, Comments
# Register your models here.


class EmployeeEvalView(admin.ModelAdmin):
    
    def employee_name(self,obj):
        return obj.employee.last_name + ', ' + obj.employee.first_name  +' (' + obj.employee.nick_name +')'

    list_display = ('employee','employee_name','user_submit','lead_submit','yr','period')
    search_fields=('employee__last_name','employee__first_name','empl__middle_name','empl__nickname')
    list_filter=['yr','period']

admin.site.register(EmployeeEval,EmployeeEvalView)

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


class EvaluationView(admin.ModelAdmin):
    
    list_display=('employee', 'criteria', 'area_lead', 'project_lead', 'manager')
    list_filter=('employee',)


admin.site.register(Evaluation,EvaluationView)



class CommentsView(admin.ModelAdmin):
    def employee_name(self,obj):
        return obj.employee.last_name + ', ' + obj.employee.first_name  +' (' + obj.employee.nick_name +')'

    list_display=('employee_name','yr','status')
    list_filter =('yr','status')
    search_fields=('employee__last_name','employee__first_name','empl__middle_name','empl__nickname')

admin.site.register(Comments, CommentsView)