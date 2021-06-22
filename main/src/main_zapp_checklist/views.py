from django.shortcuts import render
from main_hr.models import hr_master
import datetime
from .forms import health_checklistForm
from .models import health_checklist
from main.Utils import getuname
# Create your views here.
def index(request, mhiid):

    user = getuname(request)
    context = {}

    
    context.update({'uname' : user})
    if len(hr_master.objects.filter(mhi_id=mhiid)) == 0:
        return render(request, 'tracking/error.html')
    else:
        user = hr_master.objects.get(mhi_id=mhiid)
        context.update({'user' : user})
        td=datetime.datetime.now().date()
        bd = user.birth_date
        age = int((td-bd).days /365.25)
        context.update({'age' : age })
        context.update({'td' : td })

        if len(health_checklist.objects.filter(employee__mhi_id=mhiid).filter(checklist_date=td)) == 0:
            pk = hr_master.objects.get(mhi_id=mhiid).idno
            s = health_checklist.objects.create(employee_id=pk, checklist_date=td)
            s.save()
            
        checklist = health_checklist.objects.get(employee__mhi_id=mhiid, checklist_date=td)
        form = health_checklistForm(instance=checklist)
        if request.method =='POST':    
            form =health_checklistForm(request.POST or None, instance=checklist)
            if form.is_valid():
                form.save()
                return render(request, 'tracking/startwork.html')

        context.update ({'form' : form }) 
        
    return render(request, 'tracking/index.html', context)


def report(request):
    context={}
    hr = hr_master.objects.exclude(employee_status='Resigned').exclude(employee_status=
        'Terminated').exclude(employee_status='Admin').exclude(project='Rehab').order_by('nick_name')
    context.update({'hr' : hr })

    for i in hr:
        context.update({i:{'name' : i.nick_name}})
    
    
        


    return render(request,'tracking/checklist_report.html', context)
