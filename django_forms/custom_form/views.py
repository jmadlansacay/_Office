from django.shortcuts import render, redirect
from .forms import HrMasterCustom
from hr.models import HrMaster

# Create your views here.
def customform(request):
    # hr=HrMaster.objects.get(employee_id='0119')
    # form = HrMasterCustom(instance=hr)
    form = HrMasterCustom()

    if request.method =='POST':     
        form =HrMasterCustom(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('list_form')
    context = {'form' : form }

    return render (request,'custom_form/customform.html', context)


def listform(request):
    hr = HrMaster.objects.all()
    context = {'hr' : hr}

    return render (request,'custom_form/list.html', context)


def editform(request, pk):
    hr=HrMaster.objects.get(id=pk)
    form = HrMasterCustom(instance=hr)
    
    if request.method =='POST':
        print(pk) 
        hr=HrMaster.objects.get(id=pk)   
        form =HrMasterCustom(request.POST or None,instance=hr)
        if form.is_valid():
            form.save()
            return redirect('list_form')
    context = {'form' : form }

    return render (request,'custom_form/editform.html', context)