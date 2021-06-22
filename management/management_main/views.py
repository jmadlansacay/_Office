from django.shortcuts import render
from .models import *
from django.db.models import Count

def index(request):
    context = {}
    
    empl = Employees.objects.values('project__name').annotate(cnt=Count('last_name'))
    context.update({'empl' : empl })
    empl_total = Employees.objects.all().count()
    context.update({'empl_total' : empl_total })

    projecthours = ProjectHours.objects.filter(year=2020)
    context.update({'projecthours' : projecthours })

    
    return render(request, 'management_main/index.html', context)



def employees(request, wrd):
    context = {}
    word = wrd
    
    if word == 'ALL':
        employees = Employees.objects.filter()
    else:
        employees = Employees.objects.filter(project__name=word)
    
    context.update({'employees' : employees})

    return render(request, 'management_main/employees.html', context)
