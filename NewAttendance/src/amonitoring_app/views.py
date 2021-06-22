from django.shortcuts import render
from amonitoring.Utils import getuname
from amonitoring_accounts.models import user_detail
from amonitoring_main.models import MainHrHrMaster
import datetime
from datetime import date
from .models import transacations, transaction_info
from django.http import JsonResponse
# Create your views here.
def index(request):
    context = {}
    dt=datetime.date.today()
    context.update({'dt':dt})
    a=user_detail.objects.exclude(remarks='EXCLUDE').order_by('nick_name')
    attend=[]

    for i in a:
        color = 'red'
        if len(transaction_info.objects.filter(employeeid=i.employee_id).filter(timesheetdate=dt).filter(halfday=1)) != 0:
            if len(transaction_info.objects.get(employeeid=i.employee_id, timesheetdate=dt, halfday=1).reason) !=0:
                color = 'orange'
                
        if len(transacations.objects.filter(employeeid=i.employee_id).filter(timesheetdate=dt).filter(inout=0)) != 0 :
            color = 'green'
            
        if len(transacations.objects.filter(employeeid=i.employee_id).filter(timesheetdate=dt).filter(inout=1)) != 0 :          
            color = 'red'
        
        if i.remarks == 'WFH':
            color ='blue'

        info = {
            'nick_name' : i.nick_name,
            'color' :color,
            'employee_id' : i.employee_id,
            'pic' : i.pic
        }
        attend.append(info)



    context.update({'attend' : attend })
   

    return render(request,'amonitoring_app/attendance.html', context)


def error(request):
    context = {}
    context.update({'loc' : 'Error Page'})
    
    return render(request,'amonitoring_app/error.html', context)


def attendance_api(request, proj):
    context = {}
    dt=datetime.date.today()
    a=user_detail.objects.filter(project=proj).exclude(remarks='EXCLUDE').order_by('nick_name')
    attend=[]

    for i in a:
        
        color = 'red'
        if len(transaction_info.objects.filter(employeeid=i.employee_id).filter(timesheetdate=dt).filter(halfday=1)) != 0:
            if len(transaction_info.objects.get(employeeid=i.employee_id, timesheetdate=dt, halfday=1).reason) !=0:
                color = 'orange'
                
        if len(transacations.objects.filter(employeeid=i.employee_id).filter(timesheetdate=dt).filter(inout=0)) != 0 :
            color = 'green'
            
        if len(transacations.objects.filter(employeeid=i.employee_id).filter(timesheetdate=dt).filter(inout=1)) != 0 :          
            color = 'red'
        
        if i.remarks == 'WFH':
            color ='blue'

        info = {
            'nick_name' : i.nick_name,
            'color' :color,
            'employee_id' : i.employee_id,
            'pic' : i.pic
        }
        attend.append(info)
    context.update({'attend': attend})

    return JsonResponse(data=context)


def attendance_details(request, idno):
    context = {}
    dt=datetime.date.today()
    context.update({'dt': dt})
    if len(user_detail.objects.filter(employee_id=idno)) !=0:
        udetails = user_detail.objects.get(employee_id=idno)
        context.update({'udetails': udetails})


    return render(request , 'amonitoring_app/attendance_details.html', context)



def HrSync(request):

    context = {}
    uname = getuname(request)
    udetails = user_detail.objects.get(mhi_id=uname)
    context.update({'udetails' : udetails})
    context.update({'loc' : 'Sync'})

    print(udetails.access_id)
    if udetails.access_id != 1:
        context.update({'error' : 'You are not allowed'})
        return render(request,'amonitoring_app/error.html', context)

    a = MainHrHrMaster.objects.using('main').all()

    for i in a: 
        emplstat = str(i.employee_status)
        
        if emplstat == 'Resigned' or emplstat == 'Terminated' :
            if len(user_detail.objects.filter(mhi_id=i.mhi_id)) !=0:
                d = user_detail.objects.get(mhi_id=i.mhi_id)
                d.delete()
        else:
            if len(user_detail.objects.filter(mhi_id=i.mhi_id)) == 0:
                b = user_detail(mhi_id=i.mhi_id, last_name= i.last_name, first_name=i.first_name,
                    nick_name=i.nick_name, pic=i.picture, access_id=3, employee_id=i.idno, project=i.project.project_code_description )
                b.save()
            else:
                d = user_detail.objects.get(mhi_id=i.mhi_id)
                #d.project = i.project.project_code_description
                d.employee_id = i.idno
                d.first_name = i.first_name
                d.last_name = i.last_name
                d.nick_name = i.nick_name
                d.save()
                
    return render(request,'amonitoring_app/sync.html', context)
    
