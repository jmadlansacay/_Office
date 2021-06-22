from django.shortcuts import render, redirect
from .models import HrMaster, HrMasterPayrollDetail, EmployeeEval
from .forms import  HrMasterPayrollDetailForm, EmployeeEvalForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from .models import UserDetail, EmployeeEval
import csv
from django.http import HttpResponse
import xlwt
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from HReval.Util import getuname
# Create your views here.


def index(request):

    # # login check start
    # if not request.user.is_authenticated :
    #     return redirect('mylogin')
    # # login check end
    context={}
    if request.user.username == 'admin':
        return render(request, 'HReval_eval/admin.html')

    usr =getuname(request)
 
    perm = UserDetail.objects.get(user_id__username=usr).permission
    pj = UserDetail.objects.get(user_id__username=usr).project_code.id
    eid = UserDetail.objects.get(user_id__username=usr).employee.employee_id
      
    context.update({'perm' : perm })
    
    if perm=='3':
        hrmaster = EmployeeEval.objects.filter(empl_eval__project_code=pj).filter(lead_submit='On-Going')
        return redirect('dashboard')
    elif perm=='2':
        hrmaster =EmployeeEval.objects.all()
        return redirect('dashboard')
    elif perm=='4':
        hrmaster =EmployeeEval.objects.all()
        return redirect('dashboard')
    elif perm=='5':
        hrmaster =EmployeeEval.objects.all()
        return redirect('dashboard')
    else:
        return redirect('skills_map', wrd=eid)
        
    context.update({'hrmaster':hrmaster})

    return render(request, 'HReval_eval/index.html', context)

def performance(request):

    usr =getuname(request)

    context={}
    if request.user.username == 'admin':
        return render(request, 'HReval_eval/admin.html')

    perm = UserDetail.objects.get(user_id__username=usr).permission
    pj = UserDetail.objects.get(user_id__username=usr).project_code.id
    eid = UserDetail.objects.get(user_id__username=usr).employee.employee_id
    context.update({'perm' : perm })
    print(perm)
    if perm=='3':
        hrmaster = EmployeeEval.objects.filter(empl_eval__project_code=pj).filter(lead_submit='On-Going')
    elif perm=='5':
        hrmaster =EmployeeEval.objects.exclude(empl_eval__employee_id='0000').exclude(empl_eval__employee_id='0018')
    else:
        return redirect('skills_map', wrd=eid)
        
    context.update({'hrmaster':hrmaster})

    return render(request, 'HReval_eval/index.html', context)


def evaluation(request,id):

    # # login check start
    # if not request.user.is_authenticated :
    #     return redirect('mylogin')
    # # login check end
    usr =getuname(request)
    context ={}
    perm = UserDetail.objects.get(user_id__username=usr).permission
    context.update({'perm' : perm})
    if perm=='0':
        return redirect('error')
    elif perm=='3':
        if EmployeeEval.objects.get(empl_eval=id).lead_submit == 'Submitted':        
            return redirect('error')

    hrmaster = HrMaster.objects.get(id=id)
    context.update({'hrmaster' : hrmaster})
    
    hrMasterPayrollDetail =HrMasterPayrollDetail.objects.get(empl_payroll=id)

    context.update({'HrMasterPayrollDetail':hrMasterPayrollDetail})

    if len(EmployeeEval.objects.filter(empl_eval=id)) !=0:
        EmployeeEvalinstance = EmployeeEval.objects.get(empl_eval=id)
        form = EmployeeEvalForm(instance=EmployeeEvalinstance)
    else:
        form = EmployeeEvalForm()

    if request.method =='POST':
        form =EmployeeEvalForm(request.POST or None, instance=EmployeeEvalinstance)
        if form.is_valid():
            form.save()   
            return redirect('index')
        else:
            print(form.errors)

    context.update({'form' : form})

    return render(request, 'HReval_eval/Evaluation.html', context)





def mylogin(request):

        if request.method == 'POST' :   
            usertxt = request.POST.get('username')
            upasstxt = request.POST.get('password')

            if usertxt != "" and upasstxt != "" :
                user = authenticate(username=usertxt, password=upasstxt)

                if user != None :
                    login(request, user)
                    return redirect('index')

        return render(request, 'HReval_eval/Login.html')




def mylogout(request):

        logout(request)
        
        return redirect('mylogin')




def change_password(request):

    # login check start
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end
    
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('mylogin')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'HReval_eval/changepass.html', {'form': form})



    
def regular_emp(request, wrd):
    
    # # login check start
    # if not request.user.is_authenticated :
    #     return redirect('mylogin')
    # # login check end
    # # hrmaster = HrMaster.objects.get()
    usr =getuname(request)

    eid = UserDetail.objects.get(user_id__username=usr).employee.employee_id
    if wrd != eid:
        return redirect('error')

    context ={}
    perm = UserDetail.objects.get(user_id=request.user.id).permission
    context.update({'perm' : perm})
    eid = HrMaster.objects.get(employee_id=wrd).id

    hrmaster = HrMaster.objects.get(id=eid)
    context.update({'hrmaster' : hrmaster})

    EmployeeEvalinstance = EmployeeEval.objects.get(empl_eval__employee_id=wrd)

    context.update({'EmployeeEvalinstance' : EmployeeEvalinstance})

    if len(EmployeeEval.objects.filter(empl_eval__employee_id=wrd)) !=0:
        EmployeeEvalinstance = EmployeeEval.objects.get(empl_eval__employee_id=wrd)
        form = EmployeeEvalForm(instance=EmployeeEvalinstance)
    else:
        form = EmployeeEvalForm()

    if request.method =='POST':
        print('1_')
        form =EmployeeEvalForm(request.POST or None, instance=EmployeeEvalinstance)
        if form.is_valid():
            form.save()   
            return redirect('performance')
        else:
            print(form.errors)

    context.update({'form' : form})
   
    return render(request, 'HReval_eval/regular_emp.html', context)




def error_msg(request):
    return render( request, 'HReval_eval/Message.html')




# def export_users_csv(request):
#     evaluators = UserDetail.objects.filter(permission='3')
    
#     # return redirect ('error')
#     response = HttpResponse(content_type='application/ms-excel')
#     response['Content-Disposition'] = 'attachment; filename="users.xls"'

    

#     wb = xlwt.Workbook(encoding='utf-8')


#     for evaluator in evaluators:
        
#         ws = wb.add_sheet(evaluator.employee.nickname)

#         # Sheet header, first row
#         row_num = 0

#         font_style = xlwt.XFStyle()
#         font_style.font.bold = True

#         columns = ['Employee ID','Last Name', 'First name', 'Nickname', 'Speed', 'Quality', 'Efficiency', 'PDCA', 'Punctuality', 'Cooperativeness', 'Cost Saving Mind',
#             'Loyalty', 'Team Player', 'Contributions', 'Achievements']

#         for col_num in range(len(columns)):
#             ws.write(row_num, col_num, columns[col_num], font_style)

#         # Sheet body, remaining rows
#         font_style = xlwt.XFStyle()

#         # rows = User.objects.all().values_list('username', 'first_name', 'last_name', 'email')

#         rows = EmployeeEval.objects.filter(empl_eval__project_code=evaluator.project_code).exclude(empl_eval__employee_id='0000').exclude(empl_eval__employee_id='0018').values_list('empl_eval__employee_id','empl_eval__last_name',
#             'empl_eval__first_name','empl_eval__nickname','speed','accqlty', 'workeff','pdacycle', 'time_panctuality' ,'cooperativeness', 'costsaving', 'loyalty',
#             'team_player', 'contribution', 'achievement')
#         for row in rows:
#             row_num += 1
#             for col_num in range(len(row)):
#                 ws.write(row_num, col_num, row[col_num], font_style)

#     wb.save(response)
#     return response
def export_users_csv(request):

    evaluators = UserDetail.objects.filter(permission='3')
    
    # return redirect ('error')
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'

    

    wb = xlwt.Workbook(encoding='utf-8')


    for evaluator in evaluators:
        
        ws = wb.add_sheet(evaluator.employee.nickname)

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['Employee ID','Last Name', 'First name', 'Nickname','Basic', 'Fringe', 'Perf. Allow.', 'Speed', 'Quality', 'Efficiency', 'PDCA', 'Punctuality', 'Cooperativeness', 'Cost Saving Mind',
            'Harmony','Loyalty', 'Team Player','Score', 'Contributions', 'Achievements']

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()

     
        # hr = HrMaster.objects.select_related('hrmasterpayrolldetail')
        # for i in hr:
        #     print(i.hrmasterpayrolldetail.fringe)
        

    
        empl_rows = EmployeeEval.objects.filter(empl_eval__project_code=evaluator.project_code).exclude(empl_eval__employee_id='0000').exclude(empl_eval__employee_id='0018').values_list('empl_eval__employee_id','empl_eval__last_name',
            'empl_eval__first_name','empl_eval__nickname','speed','accqlty', 'workeff','pdacycle', 'time_panctuality' ,'cooperativeness', 'costsaving', 'harmony' , 'loyalty',
            'team_player', 'contribution', 'achievement')


        rows=[]
        for empl in empl_rows:            
            payrolldetail = HrMasterPayrollDetail.objects.get(empl_payroll__employee_id=empl[0])
            score=int(empl[4])+ int(empl[5])+ int(empl[6])+ int(empl[7])+ int(empl[8])+ int(empl[9])+ int(empl[10])+ int(empl[11])+ int(empl[12])+int(empl[13])
            rows.append((empl[0], empl[1], empl[2], empl[3], payrolldetail.basic, payrolldetail.fringe * 2, payrolldetail.performance_allowance, 
                int(empl[4]), int(empl[5]), int(empl[6]), int(empl[7]), int(empl[8]), int(empl[9]), int(empl[10]), int(empl[11]), int(empl[12]),int(empl[13]) , score, empl[14], empl[15]))


        
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response