from django.shortcuts import render, redirect
from .models import user_detail, tbl_icn
from ims.Utils import getuname
import os
from django.conf import settings
from django.http import JsonResponse
# Create your views here.

def index(request):
      
    user = getuname(request)
    context = {}
    uname = user_detail.objects.get(username=user)
    full_name = uname.last_name+', '+uname.first_name
    context.update({'full_name' : full_name})
    pic = uname.pic
    context.update({'pic' : pic})
    if uname.user_access_id in ['Area Lead',]:
        if uname.user_access_id == 'Area Lead':
            tblicn = tbl_icn.objects.filter(area_lead=uname.nickname)
        else:
            tblicn = tbl_icn.objects.filter(location=uname.nickname)
        context.update({'tblicn' : tblicn})
        designer = user_detail.objects.filter(user_access__id=9)
        context.update({'designer' : designer})
        checker = user_detail.objects.filter(user_access__id=7)
        context.update({'checker' : checker})
        arealead = user_detail.objects.filter(user_access__id=6)
        context.update({'arealead' :arealead})
        sv = user_detail.objects.filter(user_access__id=5)
        context.update({'sv' :sv})
  

    return render(request, 'ims_main/dashboard.html',context)


def error(request):
    return render(request, 'ims_main/error.html')



def geticninfo(request, icn):
    context = {}
    icn_info = tbl_icn.objects.get(icn=icn)
    context.update({'designer' : icn_info.designer.pic})
    context.update({'des_name' : icn_info.designer.nickname} )
    context.update({'checker' : icn_info.checker.pic})
    context.update({'checker_name' : icn_info.checker.nickname})
    context.update({'arealead' : icn_info.area_lead.pic})
    context.update({'arealead_name' : icn_info.area_lead.nickname})
    context.update({'sv' : icn_info.mhi_sv.pic})
    context.update({'sv_name' : icn_info.mhi_sv.nickname})
    
    # if len(tbl_note1.objects.filter(icn_id=icn_info.id)) != 0:
    #     note1_info = tbl_note1.objects.get(icn_id=icn_info.id)
    #     rev0 = ('-' if note1_info.rev0 is None else note1_info.rev0) 
    #     rev1 = ('-' if note1_info.rev1 is None else note1_info.rev1) 
    #     rev2 = ('-' if note1_info.rev2 is None else note1_info.rev2) 
    #     rev3 = ('-' if note1_info.rev3 is None else note1_info.rev3) 
    #     rev4 = ('-' if note1_info.rev4 is None else note1_info.rev4) 
    #     rev5 = ('-' if note1_info.rev5 is None else note1_info.rev5) 
    #     rev6 = ('-' if note1_info.rev6 is None else note1_info.rev6) 
    # else:
    #     rev0 = '-'
    #     rev1 = '-'
    #     rev2 = '-'
    #     rev3 = '-'
    #     rev4 = '-'
    #     rev5 = '-'
    #     rev6 = '-'

    # context.update({'rev0' : rev0})
    # context.update({'rev1' : rev1})
    # context.update({'rev2' : rev2})
    # context.update({'rev3' : rev3})
    # context.update({'rev4' : rev4})
    # context.update({'rev5' : rev5})
    # context.update({'rev6' : rev6})


    return JsonResponse(data=context)



def change_location(request, icn, uname):
    
    if request.method=="POST":



        user_id = getuname(request)
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
    