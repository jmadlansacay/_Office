from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.db.models import Count, Q, Sum, F
from datetime import datetime, timedelta, date
from management.Utils import getuname


def index(request):
    context = {}
    
    
    empl = Employees.objects.values('project__name').annotate(
        cnt=Count('last_name')).exclude(project__isnull=True).annotate(
            reg=Count('employee_status', filter=Q(employee_status=1))).annotate(
            proj=Count('employee_status', filter=Q(employee_status=2))).annotate(
            fix=Count('employee_status', filter=Q(employee_status=3))).annotate(
            cons=Count('employee_status', filter=Q(employee_status=4))).annotate(
            ap=Count('employee_status', filter=Q(employee_status=5))).annotate(
            prob=Count('employee_status', filter=Q(employee_status=6))).annotate(
            outsc=Count('employee_status', filter=Q(employee_status=7)))
    context.update({'empl' : empl })

    headcount = HeadCount.objects.all().order_by('-date')[:1]
    context.update({'headcount':headcount})

    fili = Employees.objects.exclude(project__isnull=True).exclude(employee_status=8).filter(nationality=1).order_by('project')
    context.update({'fili': fili})
   

    fil = Employees.objects.exclude(project__isnull=True).exclude(employee_status=8).filter(nationality=1).count()
    context.update({'fil': fil})

    jap = Employees.objects.exclude(project__isnull=True).exclude(employee_status=8).filter(nationality=2).count()
    context.update({'jap': jap})

    regular = Employees.objects.exclude(employee_status=8).filter(nationality=1).filter(employee_status=1).count()
    context.update({'regular':regular})

    all_regular = Employees.objects.exclude(employee_status=8).filter(employee_status=1).count()
    context.update({'all_regular':all_regular})

    regular_jap = Employees.objects.exclude(employee_status=8).filter(nationality=2).filter(employee_status=1).count()
    context.update({'regular_jap':regular_jap})

    project = Employees.objects.exclude(employee_status=8).filter(nationality=1).filter(employee_status=2).count()
    context.update({'project':project})

    all_project = Employees.objects.exclude(employee_status=8).filter(employee_status=2).count()
    context.update({'all_project':all_project})

    project_jap = Employees.objects.exclude(employee_status=8).filter(nationality=2).filter(employee_status=2).count()
    context.update({'project_jap':project_jap})

    fixed = Employees.objects.exclude(employee_status=8).filter(employee_status=3).count()
    context.update({'fixed':fixed})

    outsrcd = Employees.objects.exclude(employee_status=8).filter(employee_status=7).count()
    context.update({'outsrcd':outsrcd})

    outsourced_count = Employees.objects.exclude(employee_status=8).filter(employee_type=3).count()
    context.update({'outsourced_count':outsourced_count})

    indirect_outsourced_count = Employees.objects.exclude(employee_status=8).filter(employee_type=4).count()
    context.update({'indirect_outsourced_count':indirect_outsourced_count})

    empl_total = Employees.objects.exclude(project__isnull=True).exclude(employee_status=8).count()
    context.update({'empl_total' : empl_total })




    projecthours = ProjectHours.objects.filter(year=2020)
    context.update({'projecthours' : projecthours })

    jan20_sum = projecthours.aggregate(jan20=Sum('jan_hrs')).get('jan20')
    context.update({'jan20_sum' : jan20_sum })

    feb20_sum = projecthours.aggregate(feb20=Sum('feb_hrs')).get('feb20')
    context.update({'feb20_sum' : feb20_sum })

    mar20_sum = projecthours.aggregate(mar20=Sum('mar_hrs')).get('mar20')
    context.update({'mar20_sum' : mar20_sum })

    apr20_sum = projecthours.aggregate(apr20=Sum('apr_hrs')).get('apr20')
    context.update({'apr20_sum' : apr20_sum })

    may20_sum = projecthours.aggregate(may20=Sum('may_hrs')).get('may20')
    context.update({'may20_sum' : may20_sum })

    jun20_sum = projecthours.aggregate(jun20=Sum('jun_hrs')).get('jun20')
    context.update({'jun20_sum' : jun20_sum })

    jul20_sum = projecthours.aggregate(jul20=Sum('jul_hrs')).get('jul20')
    context.update({'jul20_sum' : jul20_sum })

    aug20_sum = projecthours.aggregate(aug20=Sum('aug_hrs')).get('aug20')
    context.update({'aug20_sum' : aug20_sum })

    sep20_sum = projecthours.aggregate(sep20=Sum('sep_hrs')).get('sep20')
    context.update({'sep20_sum' : sep20_sum })

    oct20_sum = projecthours.aggregate(oct20=Sum('oct_hrs')).get('oct20')
    context.update({'oct20_sum' : oct20_sum })

    nov20_sum = projecthours.aggregate(nov20=Sum('nov_hrs')).get('nov20')
    context.update({'nov20_sum' : nov20_sum })

    dec20_sum = projecthours.aggregate(dec20=Sum('dec_hrs')).get('dec20')
    context.update({'dec20_sum' : dec20_sum })

    projecthours21 = ProjectHours.objects.filter(year=2021)
    context.update({'projecthours' : projecthours })

    jan21_sum = projecthours21.aggregate(jan21=Sum('jan_hrs')).get('jan21')
    context.update({'jan21_sum' : jan21_sum })

   


    # proj_jan20 = projecthours.aggregate(jan=Sum('jan_hrs')).get('jan')
    # context.update({'proj_jan20':proj_jan20})





    employeehours = EmployeeHours.objects.filter(year=2020)
    context.update({'employeehours' : employeehours })


    nonbillable = EmployeeHours.objects.filter(year=2020).filter(employee__project_type=3)
    context.update({'nonbillable':nonbillable})

    jan_nonbill = nonbillable.aggregate(jan=Sum('jan_hrs')).get('jan')
    context.update({'jan_nonbill':jan_nonbill})

    feb_nonbill = nonbillable.aggregate(feb=Sum('feb_hrs')).get('feb')
    context.update({'feb_nonbill':feb_nonbill})

    mar_nonbill = nonbillable.aggregate(mar=Sum('mar_hrs')).get('mar')
    context.update({'mar_nonbill':mar_nonbill})

    apr_nonbill = nonbillable.aggregate(apr=Sum('apr_hrs')).get('apr')
    context.update({'apr_nonbill':apr_nonbill})

    may_nonbill = nonbillable.aggregate(may=Sum('may_hrs')).get('may')
    context.update({'may_nonbill':may_nonbill})

    jun_nonbill = nonbillable.aggregate(jun=Sum('jun_hrs')).get('jun')
    context.update({'jun_nonbill':jun_nonbill})

    jul_nonbill = nonbillable.aggregate(jul=Sum('jul_hrs')).get('jul')
    context.update({'jul_nonbill':jul_nonbill})

    aug_nonbill = nonbillable.aggregate(aug=Sum('aug_hrs')).get('aug')
    context.update({'aug_nonbill':aug_nonbill})

    sep_nonbill = nonbillable.aggregate(sep=Sum('sep_hrs')).get('sep')
    context.update({'sep_nonbill':sep_nonbill})

    oct_nonbill = nonbillable.aggregate(oct=Sum('oct_hrs')).get('oct')
    context.update({'oct_nonbill':oct_nonbill})

    nov_nonbill = nonbillable.aggregate(nov=Sum('nov_hrs')).get('nov')
    context.update({'nov_nonbill':nov_nonbill})

    dec_nonbill = nonbillable.aggregate(dec=Sum('dec_hrs')).get('dec')
    context.update({'dec_nonbill':dec_nonbill})

    nonbillable_21 = EmployeeHours.objects.filter(year=2021).filter(employee__project_type=3)
    context.update({'nonbillable_21':nonbillable_21})

    jan21_nonbill = nonbillable_21.aggregate(jan=Sum('jan_hrs')).get('jan')
    context.update({'jan21_nonbill':jan21_nonbill})

    feb21_nonbill = nonbillable_21.aggregate(feb=Sum('feb_hrs')).get('feb')
    context.update({'feb21_nonbill':feb21_nonbill})

    mar21_nonbill = nonbillable_21.aggregate(mar=Sum('mar_hrs')).get('mar')
    context.update({'mar21_nonbill':mar21_nonbill})

    apr21_nonbill = nonbillable_21.aggregate(apr=Sum('apr_hrs')).get('apr')
    context.update({'apr21_nonbill':apr21_nonbill})

    may21_nonbill = nonbillable_21.aggregate(may=Sum('may_hrs')).get('may')
    context.update({'may21_nonbill':may21_nonbill})

    jun21_nonbill = nonbillable_21.aggregate(jun=Sum('jun_hrs')).get('jun')
    context.update({'jun21_nonbill':jun21_nonbill})

    jul21_nonbill = nonbillable_21.aggregate(jul=Sum('jul_hrs')).get('jul')
    context.update({'jul21_nonbill':jul21_nonbill})

    aug21_nonbill = nonbillable_21.aggregate(aug=Sum('aug_hrs')).get('aug')
    context.update({'aug21_nonbill':aug21_nonbill})

    sep21_nonbill = nonbillable_21.aggregate(sep=Sum('sep_hrs')).get('sep')
    context.update({'sep21_nonbill':sep21_nonbill})

    oct21_nonbill = nonbillable_21.aggregate(oct=Sum('oct_hrs')).get('oct')
    context.update({'oct21_nonbill':oct21_nonbill})

    nov21_nonbill = nonbillable_21.aggregate(nov=Sum('nov_hrs')).get('nov')
    context.update({'nov21_nonbill':nov21_nonbill})
    
    dec21_nonbill = nonbillable_21.aggregate(dec=Sum('dec_hrs')).get('dec')
    context.update({'dec21_nonbill':dec21_nonbill})



    billable = EmployeeHours.objects.filter(year=2020).filter(Q(employee__project_type=1) | Q(employee__project_type=2)) 
    context.update({'billable':billable})

    jan_billable = billable.aggregate(jan=Sum('jan_hrs')).get('jan')
    context.update({'jan_billable':jan_billable})

    feb_billable = billable.aggregate(feb=Sum('feb_hrs')).get('feb')
    context.update({'feb_billable':feb_billable})

    mar_billable = billable.aggregate(mar=Sum('mar_hrs')).get('mar')
    context.update({'mar_billable':mar_billable})

    apr_billable = billable.aggregate(apr=Sum('apr_hrs')).get('apr')
    context.update({'apr_billable':apr_billable})

    may_billable = billable.aggregate(may=Sum('may_hrs')).get('may')
    context.update({'may_billable':may_billable})

    jun_billable = billable.aggregate(jun=Sum('jun_hrs')).get('jun')
    context.update({'jun_billable':jun_billable})

    jul_billable = billable.aggregate(jul=Sum('jul_hrs')).get('jul')
    context.update({'jul_billable':jul_billable})

    aug_billable = billable.aggregate(aug=Sum('aug_hrs')).get('aug')
    context.update({'aug_billable':aug_billable})

    sep_billable = billable.aggregate(sep=Sum('sep_hrs')).get('sep')
    context.update({'sep_billable':sep_billable})

    oct_billable = billable.aggregate(oct=Sum('oct_hrs')).get('oct')
    context.update({'oct_billable':oct_billable})

    nov_billable = billable.aggregate(nov=Sum('nov_hrs')).get('nov')
    context.update({'nov_billable':nov_billable})

    dec_billable = billable.aggregate(dec=Sum('dec_hrs')).get('dec')
    context.update({'dec_billable':dec_billable})

    billable_21 = EmployeeHours.objects.filter(year=2021).filter(Q(employee__project_type=1) | Q(employee__project_type=2)) 
    context.update({'billable_21':billable_21})

    jan21_billable = billable_21.aggregate(jan=Sum('jan_hrs')).get('jan')
    context.update({'jan21_billable':jan21_billable})

    feb21_billable = billable_21.aggregate(feb=Sum('feb_hrs')).get('feb')
    context.update({'feb21_billable':feb21_billable})

    mar21_billable = billable_21.aggregate(mar=Sum('mar_hrs')).get('mar')
    context.update({'mar21_billable':mar21_billable})

    apr21_billable = billable_21.aggregate(apr=Sum('apr_hrs')).get('apr')
    context.update({'apr21_billable':apr21_billable})

    may21_billable = billable_21.aggregate(may=Sum('may_hrs')).get('may')
    context.update({'may21_billable':may21_billable})

    jun21_billable = billable_21.aggregate(jun=Sum('jun_hrs')).get('jun')
    context.update({'jun21_billable':jun21_billable})

    jul21_billable = billable_21.aggregate(jul=Sum('jul_hrs')).get('jul')
    context.update({'jul21_billable':jul21_billable})

    aug21_billable = billable_21.aggregate(aug=Sum('aug_hrs')).get('aug')
    context.update({'aug21_billable':aug21_billable})

    sep21_billable = billable_21.aggregate(sep=Sum('sep_hrs')).get('sep')
    context.update({'sep21_billable':sep21_billable})

    oct21_billable = billable_21.aggregate(oct=Sum('oct_hrs')).get('oct')
    context.update({'oct21_billable':oct21_billable})

    nov21_billable = billable_21.aggregate(nov=Sum('nov_hrs')).get('nov')
    context.update({'nov21_billable':nov21_billable})

    dec21_billable = billable_21.aggregate(dec=Sum('dec_hrs')).get('dec')
    context.update({'dec21_billable':dec21_billable})














    employee = Employees.objects.all().exclude(project__isnull=True)
    context.update({'employee' : employee })

    direct_emp = employee.filter(project_type=1).exclude(employee_type=3).count()
    context.update({'direct_emp': direct_emp})

    indirect_emp = employee.filter(Q(project_type=2) | Q(project_type=3)).count()
    context.update({'indirect_emp': indirect_emp})

    outsourced = employee.filter(employee_type=3).count()
    context.update({'outsourced': outsourced})



    cov_latest = Covid.objects.all().order_by('-date')[:1]
    context.update({'cov_latest':cov_latest})    

    cov = Covid.objects.order_by('-date').filter(date__day='28')[:2]
    context.update({'cov': cov})

    covid_cases_beds = Covid.objects.all().order_by('-date')[:1]
    context.update({'covid_cases_beds':covid_cases_beds})

    

    events = Events.objects.all().order_by('-date')
    context.update({'events':events})

    messages = Managers.objects.all().order_by('-date')
    context.update({'messages':messages})

    
   
   

        
    return render(request, 'management_main/index.html', context)



def employees(request, wrd):
    context = {}
    word = wrd
    
    
    if word == 'ALL':
        employees = Employees.objects.filter()

    else:
        employees = Employees.objects.filter(project__name=word)
    
    context.update({'employees' : employees})

    jap = Employees.objects.exclude(project__isnull=True).exclude(employee_status=8).filter(nationality=2)
    context.update({'jap': jap})

    fil = Employees.objects.exclude(project__isnull=True).exclude(employee_status=8).filter(nationality=1).order_by('project')
    context.update({'fil': fil})

    direct_emp = Employees.objects.filter(Q(project_type=1) | Q(project_type=2)).exclude(employee_status=8).exclude(employee_type=3).order_by('project')
    context.update({'direct_emp': direct_emp})

    indirect_emp = Employees.objects.exclude(employee_status=8).filter(project_type=3).order_by('project')
    context.update({'indirect_emp': indirect_emp})

    outsourced = Employees.objects.exclude(employee_status=8).filter(employee_type=3).order_by('project')
    context.update({'outsourced': outsourced})

    indirect_outsourced = Employees.objects.exclude(employee_status=8).filter(employee_type=4).order_by('project')
    context.update({'indirect_outsourced': indirect_outsourced})

    direct_count = Employees.objects.exclude(employee_status=8).filter(employee_type=1).count()
    context.update({'direct_count':direct_count})

    empl = Employees.objects.values('project__name').annotate(
        cnt=Count('last_name')).exclude(project__isnull=True).exclude(employee_status=8).annotate(
            reg=Count('employee_status', filter=Q(employee_status=1))).annotate(
            proj=Count('employee_status', filter=Q(employee_status=2))).annotate(
            fix=Count('employee_status', filter=Q(employee_status=3))).annotate(
            cons=Count('employee_status', filter=Q(employee_status=4))).annotate(
            ap=Count('employee_status', filter=Q(employee_status=5))).annotate(
            prob=Count('employee_status', filter=Q(employee_status=6)))
    context.update({'empl' : empl })

  

    direct_count = Employees.objects.exclude(project__isnull=True).exclude(employee_status=8).exclude(project_type=3).exclude(employee_status=7).count()
    context.update({'direct_count':direct_count})

    indirect_count = Employees.objects.exclude(project__isnull=True).exclude(employee_status=8).filter(project_type=3).count()
    context.update({'indirect_count':indirect_count})
    
    outsourced_count = Employees.objects.exclude(project__isnull=True).exclude(employee_status=8).filter(employee_type=3).count()
    context.update({'outsourced_count':outsourced_count})

    indirect_outsourced_count = Employees.objects.exclude(project__isnull=True).exclude(employee_status=8).filter(employee_type=4).count()
    context.update({'indirect_outsourced_count':indirect_outsourced_count})

    empl_total = Employees.objects.exclude(project__isnull=True).exclude(employee_status=8).count()
    context.update({'empl_total' : empl_total })


    return render(request, 'management_main/employees.html', context)


def manhours(request):
    context = {}
    
    empl = Employees.objects.values('project__name').annotate(cnt=Count('last_name'))
    context.update({'empl' : empl })

    empl_total = Employees.objects.all().count()
    context.update({'empl_total' : empl_total })

    projecthours = ProjectHours.objects.filter(year=2020)
    context.update({'projecthours' : projecthours })

    projecthours2021 = ProjectHours.objects.filter(year=2021)
    context.update({'projecthours2021' : projecthours2021 })

    
    return render(request, 'management_main/manhours.html', context)


def employeemanhours(request):
    context = {}
    
    empl = Employees.objects.values('project__name').annotate(cnt=Count('last_name'))
    context.update({'empl' : empl })

    empl_total = Employees.objects.all().count()
    context.update({'empl_total' : empl_total })

    employeehours = EmployeeHours.objects.filter(year=2020).order_by('employee__project')
    context.update({'employeehours' : employeehours })

    employeehours2021 = EmployeeHours.objects.filter(year=2021).order_by('employee__project')
    context.update({'employeehours2021' : employeehours2021 })

        
    return render(request, 'management_main/empmanhours.html', context)


def covidoverview(request,id):
    context = {}

    overview = Covid.objects.filter(id=id).annotate(
        bed_total=F('bed_occ') + F('bed_vac')).annotate(
        icu_total=F('icu_occ') + F('icu_vac')).annotate(
        isolation_total=F('isolation_occ') + F('isolation_vac')).annotate(
        ward_total=F('ward_occ') + F('ward_vac')).annotate(
        ventilator_total=F('ventilator_occ') + F('ventilator_vac'))
    context.update({'overview':overview})

    tracker = Covid.objects.all().order_by('date')
    context.update({'tracker': tracker})

    covid_pic = Covid.objects.filter(id=id)
    context.update({'covid_pic':covid_pic})

            

    return render(request, 'management_main/covid.html', context)
    

def news_events_photos(request,id):
    context = {}

    news = Events.objects.filter(id=id)
    context.update({'news':news})

    return render(request, 'management_main/newsevents.html', context)


def financial(request):
    context = {}

    financial = Financial.objects.all()
    context.update({'financial':financial})

    return render(request, 'management_main/financial.html', context)


def messages_managers(request,id):
    
    context = {}

    messages_managers = Managers.objects.filter(id=id)
    context.update({'messages_managers':messages_managers})

    return render(request, 'management_main/managers.html', context)


def message(request):

    context = {}

    return render(request, 'management_main/message.html', context)

