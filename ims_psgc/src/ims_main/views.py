from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.http import JsonResponse
from django.contrib.auth.models import User
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from  django.contrib import messages
from django.contrib.auth import update_session_auth_hash
import os

from django.templatetags.static import static
from django.conf import settings
# Create your views here.


def dashboard(request):  
    

    # path = 'C:/Bin/ip.txt'

    # webbrowser.open('file:///'+path)

    context = {}
    useraccess = user_detail.objects.get(username=request.user.id)   
    pic = useraccess.pic
    context.update({'pic' : pic })
    uname = request.user.last_name+', '+request.user.first_name
    context.update({'uname' : uname})

    path = settings.MEDIA_ROOT
    img_list = os.listdir(path + '/images')
    context.update({'images' : img_list})

    if useraccess.user_access_id == 1:
        return redirect('/admin')
    elif useraccess.user_access_id in [9,8,7,6,5]:

        if useraccess.user_access_id == 6:
            tblicn = tbl_icn.objects.filter(area_lead=useraccess.id)
        else:
            tblicn = tbl_icn.objects.filter(location=useraccess.id)
        context.update({'tblicn' : tblicn})
        designer = user_detail.objects.filter(user_access=9)
        context.update({'designer' : designer})
        checker = user_detail.objects.filter(user_access=7)
        context.update({'checker' : checker})
        arealead = user_detail.objects.filter(user_access=6)
        context.update({'arealead' :arealead})
        sv = user_detail.objects.filter(user_access=5)
        context.update({'sv' :sv})
        
        return render(request,'ims_main/dashboard.html', context)
    else:
        return render(request,'ims_main/base.html', context)

def geticninfo(request, icn):
    context = {}
    icn_info = tbl_icn.objects.get(icn=icn)
    context.update({'designer' : icn_info.designer.pic})
    context.update({'des_name' : icn_info.designer.username.username} )
    context.update({'checker' : icn_info.checker.pic})
    context.update({'checker_name' : icn_info.checker.username.username})
    context.update({'arealead' : icn_info.area_lead.pic})
    context.update({'arealead_name' : icn_info.area_lead.username.username})
    context.update({'sv' : icn_info.mhi_sv.pic})
    context.update({'sv_name' : icn_info.mhi_sv.username.username})
    
    if len(tbl_note1.objects.filter(icn_id=icn_info.id)) != 0:
        note1_info = tbl_note1.objects.get(icn_id=icn_info.id)
        rev0 = ('-' if note1_info.rev0 is None else note1_info.rev0) 
        rev1 = ('-' if note1_info.rev1 is None else note1_info.rev1) 
        rev2 = ('-' if note1_info.rev2 is None else note1_info.rev2) 
        rev3 = ('-' if note1_info.rev3 is None else note1_info.rev3) 
        rev4 = ('-' if note1_info.rev4 is None else note1_info.rev4) 
        rev5 = ('-' if note1_info.rev5 is None else note1_info.rev5) 
        rev6 = ('-' if note1_info.rev6 is None else note1_info.rev6) 
    else:
        rev0 = '-'
        rev1 = '-'
        rev2 = '-'
        rev3 = '-'
        rev4 = '-'
        rev5 = '-'
        rev6 = '-'

    context.update({'rev0' : rev0})
    context.update({'rev1' : rev1})
    context.update({'rev2' : rev2})
    context.update({'rev3' : rev3})
    context.update({'rev4' : rev4})
    context.update({'rev5' : rev5})
    context.update({'rev6' : rev6})


    return JsonResponse(data=context)


def change_location(request, icn, uname):
    if request.method=="POST":
        user_id = User.objects.get(username=uname).id
        detail_id = user_detail.objects.get(username=user_id)
        icn_info = tbl_icn.objects.get(icn=icn)
        icn_info.location = detail_id
        if detail_id.user_access.id == 9 :
            icn_info.designer = detail_id
        elif detail_id.user_access.id == 7:
            icn_info.checker = detail_id
        elif detail_id.user_access.id == 6:
            icn_info.area_lead = detail_id
        elif detail_id.user_access.id == 5:
            icn_info.sv = detail_id

        icn_info.save()
        method_id = 'POST' 
        return JsonResponse(data={'method_id' : method_id})   
    else:
        context = {}
        useraccess = user_detail.objects.get(username=request.user.id)   
        pic = useraccess.pic
        context.update({'pic' : pic })
        uname = request.user.last_name+', '+request.user.first_name
        context.update({'uname' : uname})
        return render(request, 'ims_main/forbidden.html', context)
    
    

def location_chart(request):
    context = {}
    useraccess = user_detail.objects.get(username=request.user.id)   
    pic = useraccess.pic
    context.update({'pic' : pic })
    uname = request.user.last_name+', '+request.user.first_name
    context.update({'uname' : uname})
    
    
    datnew = []
    datrev = []
    dathld = []

    designer_category = []
    designer = user_detail.objects.filter(user_access=9)
    total=0
    for i in designer:
        total = 0
        datnew.append(tbl_icn.objects.filter(location=i).filter(icn_status='NEW').count())
        total = total + tbl_icn.objects.exclude(mhi_status_id=1).filter(location=i).filter(icn_status='NEW').count()
        datrev.append(tbl_icn.objects.filter(location=i).filter(icn_status='REV').count())
        total = total + tbl_icn.objects.filter(location=i).filter(icn_status='REV').count()
        dathld.append(0)
        total = total + tbl_icn.objects.filter(mhi_status_id=1).filter(location=i).filter(icn_status='NEW').count()
        designer_category.append(i.username.username+'-'+str(total))
    context.update ({'designer_category' : designer_category})
    designerseries =[{
        'name': 'New',
        'data': datnew,
        'color': '#03fcf4'
    }, {
        'name': 'Rev',
        'data': datrev,
        'color': '#d0d3d9'
    }, {
        'name': 'Hold',
        'data': dathld,
        'color': '#f70400'
    }]
    context.update({'designerseries' :designerseries})

    checker_category = []
    checker = user_detail.objects.filter(user_access=7)
    datnew = []
    datrev = []
    dathld = []
    total=0
    for i in checker:
        total = 0
        datnew.append(tbl_icn.objects.exclude(mhi_status_id=1).filter(location=i).filter(icn_status='NEW').count())
        total = total + tbl_icn.objects.exclude(mhi_status_id=1).filter(location=i).filter(icn_status='NEW').count()
        datrev.append(tbl_icn.objects.filter(location=i).filter(icn_status='REV').count())
        total = total + tbl_icn.objects.filter(location=i).filter(icn_status='REV').count()
        dathld.append(tbl_icn.objects.filter(mhi_status_id=1).filter(location=i).filter(icn_status='NEW').count())
        total = total + tbl_icn.objects.filter(mhi_status_id=1).filter(location=i).filter(icn_status='NEW').count()
        checker_category.append(i.username.username+'-'+str(total))
    context.update ({'checker_category' : checker_category})
    checkerseries =[{
        'name': 'New',
        'data': datnew,
        'color': '#1cf211'
    }, {
        'name': 'Rev',
        'data': datrev,
        'color': '#d0d3d9'
    }, {
        'name': 'Hold',
        'data': dathld,
        'color': '#f70400'
    }]


    context.update({'checkerseries' :checkerseries})  

    return render(request, 'ims_main/location_chart.html',context)



def area_chart(request):
    context={}

    
    iss = tbl_icn.objects.filter(icn_status='NEW').filter(mhi_status__mhi_code='IS').count()
    rc = tbl_icn.objects.filter(icn_status='NEW').filter(mhi_status__mhi_code='RC').count()
    dc = tbl_icn.objects.filter(icn_status='NEW').filter(mhi_status__mhi_code='DC').count()
    total = tbl_icn.objects.filter(icn_status='NEW').count()
    sc = total - (iss+rc+dc)
    data =  [
            { 'name': 'IS', 'y': iss },
            { 'name': 'RC', 'y': rc },
            { 'name': 'DC', 'y': dc },
            { 'name': 'SC', 'y': sc },    
        ]
    context.update({'dataall' : data})
    context.update({'totalall' : total})


    iss = tbl_icn.objects.filter(unit__unit_description='COMMON').filter(icn_status='NEW').filter(mhi_status__mhi_code='IS').count()
    rc = tbl_icn.objects.filter(unit__unit_description='COMMON').filter(icn_status='NEW').filter(mhi_status__mhi_code='RC').count()
    dc = tbl_icn.objects.filter(unit__unit_description='COMMON').filter(icn_status='NEW').filter(mhi_status__mhi_code='DC').count()
    total = tbl_icn.objects.filter(unit__unit_description='COMMON').filter(icn_status='NEW').count()
    sc = total - (iss+rc+dc)
    data =  [
            { 'name': 'IS', 'y': iss },
            { 'name': 'RC', 'y': rc },
            { 'name': 'DC', 'y': dc },
            { 'name': 'SC', 'y': sc },    
        ]
    context.update({'datacommon' : data})
    context.update({'totalcommon' : total})


    iss = tbl_icn.objects.filter(unit__unit_description='CO2_CAPTURE').filter(icn_status='NEW').filter(mhi_status__mhi_code='IS').count()
    rc = tbl_icn.objects.filter(unit__unit_description='CO2_CAPTURE').filter(icn_status='NEW').filter(mhi_status__mhi_code='RC').count()
    dc = tbl_icn.objects.filter(unit__unit_description='CO2_CAPTURE').filter(icn_status='NEW').filter(mhi_status__mhi_code='DC').count()
    total = tbl_icn.objects.filter(unit__unit_description='CO2_CAPTURE').filter(icn_status='NEW').count()
    sc = total - (iss+rc+dc)
    data =  [
            { 'name': 'IS', 'y': iss },
            { 'name': 'RC', 'y': rc },
            { 'name': 'DC', 'y': dc },
            { 'name': 'SC', 'y': sc },    
        ]
    context.update({'datacap' : data})
    context.update({'totalcap' : total})


    iss = tbl_icn.objects.filter(unit__unit_description='CO2_COMPRESSION').filter(icn_status='NEW').filter(mhi_status__mhi_code='IS').count()
    rc = tbl_icn.objects.filter(unit__unit_description='CO2_COMPRESSION').filter(icn_status='NEW').filter(mhi_status__mhi_code='RC').count()
    dc = tbl_icn.objects.filter(unit__unit_description='CO2_COMPRESSION').filter(icn_status='NEW').filter(mhi_status__mhi_code='DC').count()
    total = tbl_icn.objects.filter(unit__unit_description='CO2_COMPRESSION').filter(icn_status='NEW').count()
    sc = total - (iss+rc+dc)
    data =  [
            { 'name': 'IS', 'y': iss },
            { 'name': 'RC', 'y': rc },
            { 'name': 'DC', 'y': dc },
            { 'name': 'SC', 'y': sc },    
        ]
    context.update({'datacom' : data})
    context.update({'totalcom' : total})


    iss = tbl_icn.objects.filter(unit__unit_description='UNDERGROUND').filter(icn_status='NEW').filter(mhi_status__mhi_code='IS').count()
    rc = tbl_icn.objects.filter(unit__unit_description='UNDERGROUND').filter(icn_status='NEW').filter(mhi_status__mhi_code='RC').count()
    dc = tbl_icn.objects.filter(unit__unit_description='UNDERGROUND').filter(icn_status='NEW').filter(mhi_status__mhi_code='DC').count()
    total = tbl_icn.objects.filter(unit__unit_description='UNDERGROUND').filter(icn_status='NEW').count()
    sc = total - (iss+rc+dc)
    data =  [
            { 'name': 'IS', 'y': iss },
            { 'name': 'RC', 'y': rc },
            { 'name': 'DC', 'y': dc },
            { 'name': 'SC', 'y': sc },    
        ]
    context.update({'dataug' : data})
    context.update({'totalug' : total})





    return render (request, 'ims_main/area_chart.html',context)


def loginPage(request):
    if request.user.is_authenticated:
	    return redirect('ims-dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('login')
            else:
                messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'ims_main/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def modal(request):
    return render(request,'ims_main/modal.html')


def change_password(request):


    context = {}
    useraccess = user_detail.objects.get(username=request.user.id)   
    pic = useraccess.pic
    context.update({'pic' : pic })
    uname = request.user.last_name+', '+request.user.first_name
    context.update({'uname' : uname})
    
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)

    context.update({'form' : form })

    return render(request, 'ims_main/change_password.html', context)



