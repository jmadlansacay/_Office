from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from HReval_eval.models import *
from HReval_eval.models import UserDetail
from .forms import EvaluationForm, comandsuggForm
from django.forms import inlineformset_factory, modelformset_factory
import datetime
from django.http import HttpResponse
import xlwt
from HReval.Util import getuname

# Create your views here.



def skills_map(request, wrd):

    # if not request.user.is_authenticated :
    #     return redirect('mylogin')

    usr=getuname(request)
    
    context={}
    # employeeid = UserDetail.objects.get(user=request.user).employee.employee_id
    # user = UserDetail.objects.get(user=request.user)

    employeeid = UserDetail.objects.get(user__username=usr).employee.employee_id
    user = UserDetail.objects.get(user__username=usr)
    

    skilltree = EmployeeTree.objects.get(employee=user.employee)
    context.update({'skilltree' : skilltree})
    
    if skilltree.access == 1:
        if wrd != employeeid :
            return redirect('error')

    evalinfo = EmployeeTree.objects.get(employee__employee_id=wrd)
    context.update({'evalinfo' : evalinfo})
    employee = HrMaster.objects.get(employee_id=wrd)
    context.update({'employee' : employee})
    age = int((datetime.date.today()-employee.date_of_birth).days/365)
    context.update({'age' : age})
    yos = int((datetime.date.today()-employee.date_employed).days/365)
    context.update({'yos' : yos})
    arealead = ""
    projectlead = ""
    manager = HrMaster.objects.get(employee_id='0018')
  



    if evalinfo.access == 1:
        arealead = EmployeeTree.objects.get(access=2, project_area=evalinfo.project_area).employee
        projectlead = EmployeeTree.objects.get(access=3, employee__project_code=evalinfo.employee.project_code).employee
    elif evalinfo.access == 2:
        arealead = HrMaster.objects.get(employee_id=wrd)
        projectlead = EmployeeTree.objects.get(access=3, employee__project_code=evalinfo.employee.project_code).employee
    elif evalinfo.access == 3:
        arealead = HrMaster.objects.get(employee_id=wrd)
        projectlead = HrMaster.objects.get(employee_id=wrd)

    context.update({'projectlead' : projectlead })
    context.update({'arealead' : arealead })
    context.update({'manager' : manager})
   

    criterias = EvaluationCriteria.objects.filter(group__contains=evalinfo.skill_set)
    
    for i in criterias:
        if len(Evaluation.objects.filter(employee=employee).filter(criteria=i)) == 0 :
            b = Evaluation(employee=employee,criteria=i,self_rating='#',area_lead=arealead, area_lead_rating='#',
                project_lead=projectlead, project_lead_rating='#', manager=manager, manager_rating='#', actions='')
            b.save()

    # EvaluationFormSet = modelformset_factory(Evaluation, fields=('criteria','self_rating', 'area_lead_rating','project_lead_rating', 'manager_rating'), extra=0)
    EvaluationFormSet = modelformset_factory(Evaluation, form=EvaluationForm, extra=0)

    if request.method == 'POST':
        formset = EvaluationFormSet(request.POST, queryset=Evaluation.objects.filter(employee__id=employee.id))
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.employee_id = employee.id 
                instance.save()

            return redirect ('skills_map', wrd = wrd)

    formset = EvaluationFormSet(queryset=Evaluation.objects.filter(employee__id=employee.id))

    context.update({'formset' : formset})
    return render(request,'HRskills_map/skills_eval.html', context)



def dashboard(request):

    # if not request.user.is_authenticated :
    #     return redirect('mylogin')

    context={}
    # user = UserDetail.objects.get(user=request.user)
    usr=getuname(request)
    user = UserDetail.objects.get(user__username=usr)
    context.update({'user': user})
    skilltree = EmployeeTree.objects.get(employee=user.employee)
    context.update({'skilltree' : skilltree})

    return render(request,'HRskills_map/dashboard.html', context)



def skills_list(request):

    # if not request.user.is_authenticated :
    #     return redirect('mylogin')

    usr = getuname(request)
    context={}
    user = UserDetail.objects.get(user__username=usr)
    context.update({'user': user})
    skilltree = EmployeeTree.objects.get(employee=user.employee)
    context.update({'skilltree' : skilltree})

    if skilltree.access == 1:
        return redirect('error')
    elif skilltree.access==2:
        employees = EmployeeTree.objects.filter(project_area=skilltree.project_area).exclude(employee__employee_type_id='05')
    elif skilltree.access==3:
        employees = EmployeeTree.objects.filter(employee__project_code=skilltree.employee.project_code).exclude(employee__employee_type_id='05')
    elif skilltree.access==4:
        employees = EmployeeTree.objects.filter(skill_set='OPERATION').exclude(employee__employee_type_id='05')
    elif skilltree.access==5:
        if skilltree.employee.employee_id == '0018':
            employees = EmployeeTree.objects.exclude(employee__employee_id='0018').exclude(employee__employee_type_id='05')
        else:
            employees = EmployeeTree.objects.filter(skill_set='OPERATION').exclude(employee__employee_type_id='05')
        

    context.update({'employees' : employees})
    

    return render(request,'HRskills_map/skills_list.html', context)



def export_users_csv2(request):


    usr=getuname(request)

    user = UserDetail.objects.get(user__username=usr)
    skilltree = EmployeeTree.objects.get(employee=user.employee)
    

    if skilltree.access == 1:
        return redirect('error')
    elif skilltree.access==2:
        return redirect('error')
    elif skilltree.access==3:
        return redirect('error')
    elif skilltree.access==4:
        employees = EmployeeTree.objects.filter(skill_set='OPERATION').exclude(employee__employee_type_id='05')
    elif skilltree.access==5:
        if skilltree.employee.employee_id == '0018':
            employees = EmployeeTree.objects.exclude(employee__employee_id='0018').exclude(employee__employee_type_id='05')
        else:
            employees = EmployeeTree.objects.filter(skill_set='OPERATION').exclude(employee__employee_type_id='05')

    # return redirect ('error')
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'
  

    wb = xlwt.Workbook(encoding='utf-8')

    for i in employees:
        
        ws = wb.add_sheet(i.employee.nickname)

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        ws.write(row_num, 0, i.employee.last_name+', '+i.employee.first_name+' ('+i.employee.nickname+')', font_style)

        row_num += 2
        rows = Evaluation.objects.filter(employee_id=i.employee_id)
        for a in rows:
            ws.write(row_num, 1, 'Self', font_style)
            ws.write(row_num, 2, str(a.area_lead.nickname), font_style)
            ws.write(row_num, 3, str(a.project_lead.nickname), font_style)
            ws.write(row_num, 4, str(a.manager.nickname), font_style)
            break

        row_num += 1
        columns = ['What', 'Skill Level', 'Skill Level','Skill Level', 'Skill Level', 'Action']

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

    
        
        rows = Evaluation.objects.filter(employee_id=i.employee_id).values_list('criteria__description','self_rating','area_lead_rating','project_lead_rating', 'manager_rating', 'actions')
    
        
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response



def comsugg(request):
    
    usr=getuname(request)
    
    context={}
    # employeeid = UserDetail.objects.get(user=request.user).employee.employee_id
    # user = UserDetail.objects.get(user=request.user)

    employeeid = UserDetail.objects.get(user__username=usr).employee.employee_id
    user = UserDetail.objects.get(user__username=usr)
    wrd = UserDetail.objects.get(user_id__username=usr).employee.employee_id

    skilltree = EmployeeTree.objects.get(employee=user.employee)
    context.update({'skilltree' : skilltree})
    
    
    evalinfo = EmployeeTree.objects.get(employee__employee_id=wrd)
    context.update({'evalinfo' : evalinfo})
    employee = HrMaster.objects.get(employee_id=wrd)
    context.update({'employee' : employee})
    age = int((datetime.date.today()-employee.date_of_birth).days/365)
    context.update({'age' : age})
    yos = int((datetime.date.today()-employee.date_employed).days/365)
    context.update({'yos' : yos})
    arealead = ""
    projectlead = ""
    manager = HrMaster.objects.get(employee_id='0018')
    ids = employee.employee_id
    
    abc = comandsugg.objects.all()

    print(abc)
   
    
    return render(request,'HRskills_map/comsugg.html', context)