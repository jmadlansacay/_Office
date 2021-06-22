from django.shortcuts import render, redirect
from django.views import View
from mhiap_hr_ref.util import getUserDetail, getPermission
from .models import HrMaster, HrMasterWorkDetail, HrMasterAddress, HrMasterPayrollDetail
from mhiap_hr_ref.models import EmployeeTypeCode, EmployeeStatusCode
import datetime
from .forms import HrMasterModelForm, HrMasterWorkDetailForm, HrMasterAddressForm, HrMasterPayrollDetailForm

# Create your views here.
class hr_index(View):  
    def get(self, request):
        context = {}
        udetail = getUserDetail(request.user.username)
        context.update({'udetail' : udetail })
        uname = request.user.last_name+', '+request.user.first_name
        context.update({'uname' : uname })
        if getPermission(request.user.username,'HR') == 0 :
            context.update({'error' : 'ACCESS DENIED'})
            return render(request,'mhiap_hr/hr_error.html', context)
        regular_count = HrMaster.objects.filter(employee_status_id=1).count()
        context.update({"regular_count" : regular_count})
        probationary_count = HrMaster.objects.filter(employee_status_id=2).count()
        context.update({"probationary_count" : probationary_count})
        projectbased_count = HrMaster.objects.filter(employee_status_id=5).count()
        context.update({"projectbased_count" : projectbased_count})
        fixedterm_count = HrMaster.objects.filter(employee_status_id=7).count()
        context.update({"fixedterm_count" : fixedterm_count})
        outsourced_count = HrMaster.objects.filter(employee_status_id=6).count()
        context.update({"outsourced_count" : outsourced_count})
        return render(request,'mhiap_hr/hr_index.html', context)



def hr_error(request):

    context = {}
    udetail = getUserDetail(request.user.username)
    context.update({'udetail' : udetail })
    uname = request.user.last_name+', '+request.user.first_name
    context.update({'uname' : uname })
    return render(request,'mhiap_hr/hr_error.html', context)





class hr_master(View):
    def get(self,request): 
        context = {}
        udetail = getUserDetail(request.user.username)
        context.update({'udetail' : udetail })
        uname = request.user.last_name+', '+request.user.first_name
        context.update({'uname' : uname })

        if getPermission(request.user.username,'HR') == 0 :
            context.update({'error' : 'ACCESS DENIED'})
            return render(request,'mhiap_hr/hr_error.html', context)


        hrdb = HrMaster.objects.filter().order_by('-last_name')
        context.update({'hrdb': hrdb})

        return render(request,'mhiap_hr/hr_master.html', context)


def hr_master_edit(request, pk):
    context = {}
    udetail = getUserDetail(request.user.username)
    context.update({'udetail' : udetail })
    uname = request.user.last_name+', '+request.user.first_name
    context.update({'uname' : uname })
    
    if getPermission(request.user.username,'HR') == 0 :
        context.update({'error' : 'ACCESS DENIED'})
        return render(request,'mhiap_hr/hr_error.html', context)

    hrdb=HrMaster.objects.get(id=pk)
    context.update({'hrdb' : hrdb})
    form = HrMasterModelForm(instance=hrdb)
    
    hrwork = HrMasterWorkDetail.objects.get(empl_id=pk)
    context.update({'hrwork' : hrwork})
    formwork =  HrMasterWorkDetailForm(instance=hrwork)

    hraddress = HrMasterAddress.objects.get(empl_address_id=pk)
    context.update({'hraddress' : hraddress})
    formaddress = HrMasterAddressForm(instance=hraddress)

    hrpayroll = HrMasterPayrollDetail.objects.get(empl_payroll_id=pk)
    context.update({'hrpayroll' : hrpayroll})
    formpayroll = HrMasterPayrollDetailForm(instance=hrpayroll)
    

    if request.method =='POST':
        form =HrMasterModelForm(request.POST or None, instance=hrdb)
        formwork = HrMasterWorkDetailForm(request.POST or None,  instance=hrwork)
        formaddress = HrMasterAddressForm(request.POST or None, instance=hraddress)
        formpayroll = HrMasterPayrollDetailForm(request.POST or None, instance=hrpayroll)
        if form.is_valid() and formwork.is_valid() and formaddress.is_valid() and formpayroll.is_valid():
            form.save()
            formwork.save()
            formaddress.save()
            formpayroll.save()
            return redirect('hr_master')
        else:
            print(form.errors)
            
        

    context.update({'form' : form })
    context.update({'formwork' : formwork})
    context.update({'formaddress' : formaddress})
    context.update({'formpayroll' : formpayroll})
    return render(request,'mhiap_hr/hr_master_edit.html', context)






def getactive(mnu):
    if mnu =='DB':
        return {'DB' : 'active', 'HR' : '' }
    