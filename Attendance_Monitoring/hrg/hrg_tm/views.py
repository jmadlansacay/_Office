from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from hrg_hr.models import user_detail, tblmaster, intro
from hrg_tm.models import *
import datetime
from datetime import date
import time
from django.http import JsonResponse
import json

# Create your views here.
def attendance(request, word):

    args = {}
    # uname = request.user.last_name +', '+ request.user.first_name
    # args.update({'uname' : uname})
    upic = ""
    # if len(user_detail.objects.filter(mhiid=request.user.id)) !=0 :
    #     upic = user_detail.objects.get(mhiid=request.user.id).pictureurl

    args.update({'upic' : upic})

    projcode = tblmaster.objects.raw("SELECT dbo.hrg_hr_ref_projectcode.id, dbo.hrg_hr_ref_projectcode.projectcodedesc FROM dbo.hrg_hr_tblmaster INNER JOIN dbo.hrg_hr_ref_projectcode ON dbo.hrg_hr_tblmaster.projectcode_id = dbo.hrg_hr_ref_projectcode.id WHERE (NOT (dbo.hrg_hr_tblmaster.employeestatus_id IN (3, 4))) GROUP BY dbo.hrg_hr_ref_projectcode.projectcodedesc, dbo.hrg_hr_ref_projectcode.id ORDER BY dbo.hrg_hr_ref_projectcode.projectcodedesc")

    args.update({'projcode' : projcode})

    wrd=word
    wrd=wrd.replace('attendance/','')
    args.update({'wrd' : wrd})

    if wrd=='ALL':
    
        empllist = tblmaster.objects.raw("SELECT dbo.hrg_hr_tblmaster.id, dbo.hrg_hr_tblmaster.employeeid, dbo.hrg_hr_tblmaster.nickname, dbo.hrg_hr_tblmaster.dateemployed, dbo.hrg_hr_user_detail.pictureurl , dbo.auth_user.id AS mhiid  FROM dbo.auth_user INNER JOIN dbo.hrg_hr_user_detail ON dbo.auth_user.id = dbo.hrg_hr_user_detail.mhiid_id INNER JOIN dbo.hrg_hr_tblmaster ON dbo.auth_user.username = dbo.hrg_hr_tblmaster.username WHERE (dbo.hrg_hr_tblmaster.employeestatus_id <> 3) ORDER BY dbo.hrg_hr_tblmaster.nickname")

    else:

        empllist = tblmaster.objects.raw("SELECT dbo.hrg_hr_tblmaster.id, dbo.hrg_hr_tblmaster.employeeid, dbo.hrg_hr_tblmaster.nickname, dbo.hrg_hr_tblmaster.dateemployed, dbo.hrg_hr_user_detail.pictureurl , dbo.auth_user.id AS mhiid FROM dbo.auth_user INNER JOIN dbo.hrg_hr_user_detail ON dbo.auth_user.id = dbo.hrg_hr_user_detail.mhiid_id INNER JOIN dbo.hrg_hr_tblmaster ON dbo.auth_user.username = dbo.hrg_hr_tblmaster.username INNER JOIN dbo.hrg_hr_ref_projectcode ON dbo.hrg_hr_tblmaster.projectcode_id = dbo.hrg_hr_ref_projectcode.id WHERE (dbo.hrg_hr_tblmaster.employeestatus_id <> 3) AND (dbo.hrg_hr_ref_projectcode.projectcodedesc = '"+wrd+"') ORDER BY dbo.hrg_hr_tblmaster.nickname")

    attend = []
    color = 'red'
    dt=datetime.date.today()
    
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    time_in ="19:00:00"

    
    for i in empllist:
        color = 'red'
        
        

        if len(transaction_info.objects.filter(employeeid=i.employeeid).filter(timesheetdate=dt).filter(halfday=1)) != 0:
            if len(transaction_info.objects.get(employeeid=i.employeeid, timesheetdate=dt, halfday=1).reason) !=0:
                color = 'orange'
                

        if len(transacations.objects.filter(employeeid=i.employeeid).filter(timesheetdate=dt).filter(inout=0)) != 0 :
            color = 'green'
            

        if len(transacations.objects.filter(employeeid=i.employeeid).filter(timesheetdate=dt).filter(inout=1)) != 0 :          
            color = 'red'
            

        if len(user_detail.objects.filter(mhiid_id=i.mhiid).filter(remarks='WFH')) != 0 :
            color = 'blue'
            
        if len(user_detail.objects.filter(mhiid_id=i.mhiid).filter(remarks='NS')) != 0 :
            color = '#6610f2'

            if current_time > time_in:
                if len(transacations.objects.filter(employeeid=i.employeeid).filter(timesheetdate=dt).filter(inout=0)) != 0 :
                    color = 'green'
            
                if len(transacations.objects.filter(employeeid=i.employeeid).filter(timesheetdate=dt).filter(inout=1)) != 0 :          
                    color = 'red'


        

        if i.dateemployed != 'None':           
            dy = days_between(i.dateemployed,dt)
        else:
            dy= 50
           
        if (dy < 32):
            newemp = 'new'
        else:
            newemp = 'old'



        

        attend.append([i.id,i.nickname,i.pictureurl,color,newemp])


    args.update({'attend' : attend})

    args.update({'dt': dt})


    return render (request, 'hrg_tm/attendance.html',args)



def attendance_details(request, pk):
        
    args = {}
    dt=datetime.date.today()
    args.update({'dt' : dt})
    employeeid = tblmaster.objects.get(id=pk).employeeid
    lastname = tblmaster.objects.get(id=pk).lastname
    firstname = tblmaster.objects.get(id=pk).firstname
    uname = tblmaster.objects.get(id=pk).username
    empldate = tblmaster.objects.get(id=pk).dateemployed
    uid = User.objects.get(username=uname).id
    # uid = request.META["REMOTE_USER"]
    # uid = uname.replace('MHI\\','')
    # uid ='Q034800'
    picurl = user_detail.objects.get(mhiid_id=uid).pictureurl
    dy = days_between(dt,empldate)

    args.update({'employeeid' : employeeid})
    args.update({'lastname' : lastname})
    args.update({'firstname' : firstname})
    args.update({'picurl' : picurl})
    args.update({'dy' : dy})
    
    if len(intro.objects.filter(employeeid=employeeid)) == 0:
        msg = ''
    else:
        msg = intro.objects.get(employeeid=employeeid).msg
    
    args.update({'msg' : msg })

    if len(transaction_info.objects.filter(timesheetdate=dt).filter(employeeid=employeeid)) == 0:
        halfday = ""
    else:
        halfday = transaction_info.objects.get(timesheetdate=dt,employeeid=employeeid).halfday
    
    args.update({'halfday' : halfday })
    

    time_in=''
    tin = transacations.objects.filter(timesheetdate=dt).filter(employeeid=employeeid).filter(inout=0).order_by('timepunch')
    for i in tin:
        time_in=(i.timepunch)
            
    time_out=''
    tout=transacations.objects.filter(timesheetdate=dt).filter(employeeid=employeeid).filter(inout=1).order_by('-timepunch')
    for i in tout:
        time_out=(i.timepunch)

    
    args.update({'time_in' : time_in})
    args.update({'time_out' : time_out})

    reason =''
    rson = transaction_info.objects.filter(timesheetdate=dt).filter(employeeid=employeeid)
    hd = 0
    for i in rson:
        reason = i.reason
        hd = i.halfday
    
     
    if request.method == 'POST':
        reason = request.POST.get('reason')
        hd = request.POST.get('halfday')
        if len(transaction_info.objects.filter(timesheetdate=dt).filter(employeeid=employeeid)) != 0:
            b =transaction_info.objects.get(timesheetdate=dt, employeeid=employeeid)
            b.delete()

        b = transaction_info(employeeid=employeeid, timesheetdate=dt, halfday=hd, reason=reason)
        b.save()
        return redirect('attendance_details', pk=pk)


    
    # if user_detail.objects.get(mhiid=request.user.id).user_access == 'ADMIN' or user_detail.objects.get(mhiid=request.user.id).user_access == 'ATTENDANCE_ADMIN' :
    #     args.update({'access' : 1})
    # else:
    #     args.update({'access' : 0})


    # muname = request.META["REMOTE_USER"]
    # muname = muname.replace('MHI\\','')
    muname = 'Q034800'
    muname = 'U300823'
    if len(User.objects.filter(username=muname)) != 0:
        mhid = User.objects.get(username=muname).id

        if user_detail.objects.get(mhiid=mhid).user_access == 'ADMIN' or user_detail.objects.get(mhiid=mhid).user_access == 'ATTENDANCE_ADMIN' :
            args.update({'access' : 1})
        else:
            args.update({'access' : 0})
    else:
        args.update({'access' : 0})
    
    args.update({'reason': reason})
    args.update({'hd' : hd})
    

    # if request.user.username == uname:
    #     owner = 1
    # else:
    #     owner = 0

    if muname == uname:
        owner = 1
    else:
        owner = 0
    
    args.update({'owner' : owner})
    print(args)
    return render( request,'hrg_tm/attendance_details.html',args)




def msg_update(request, word):

    args = {}
    pk=tblmaster.objects.get(employeeid=word).id
    args.update({'pk' : pk})

    if request.method == 'POST':
        msg = request.POST.get("Message")
        
        if len(intro.objects.filter(employeeid=word)) == 0:
            b = intro(employeeid=word, msg=msg)
            b.save()
        else:
            b = intro.objects.get(employeeid=word)
            b.msg = msg
            b.save()

        return redirect('attendance_details', pk=pk)
    
    if len(intro.objects.filter(employeeid=word)) == 0:
        msg = ''
    else:
        msg = intro.objects.get(employeeid=word).msg

    args.update({'msg' : msg })

    return render(request, 'hrg_tm/attendance_msgupdate.html', args)




def attendance2(request):

    args = {}

    dt=datetime.date.today()

    args.update({'dt' : dt})
    
    #Project Lead
    args.update({'e0111' : getcolor('0111')})
    #NH3 Area Lead
    args.update({'e0204' : getcolor('0204')})
    args.update({'e0207' : getcolor('0207')})
    #NH3 Designer
    args.update({'e0221' : getcolor('0221')})
    args.update({'e0117' : getcolor('0117')})
    args.update({'e0116' : getcolor('0116')})
    #NH3 S3D Designer
    args.update({'e0219' : getcolor('0219')})
    args.update({'e0215' : getcolor('0215')})
    args.update({'e0248' : getcolor('0248')})
    args.update({'e0263' : getcolor('0263')})
    args.update({'e0262' : getcolor('0262')})
    args.update({'e0206' : getcolor('0206')})


    #Urea Area Lead
    args.update({'e0223' : getcolor('0223')})
    #Urea Designer
    args.update({'e0229' : getcolor('0229')})
    args.update({'e0269' : getcolor('0269')})
    #Urea S3D Designer
    args.update({'e0259' : getcolor('0259')})
    args.update({'e0252' : getcolor('0252')})
    args.update({'em032' : getcolor('M032')})
    args.update({'e0258' : getcolor('0258')})



    #Utility Area Lead
    args.update({'e0216' : getcolor('0216')})
    #Utility Designer

    args.update({'em031' : getcolor('M031')})
    args.update({'e0274' : getcolor('0274')})
    #Utility S3D Designer
    args.update({'e0256' : getcolor('0256')})
    args.update({'e0271' : getcolor('0271')})
    args.update({'e0208' : getcolor('0208')})
    args.update({'e0226' : getcolor('0226')})
    args.update({'e0268' : getcolor('0268')})

    #Piperack Area Lead
    args.update({'e0217' : getcolor('0217')})
    #Piperack Designer
    args.update({'e0211' : getcolor('0211')})
    args.update({'e0246' : getcolor('0246')})
    
    #Piperack S3D Designer
    args.update({'e0203' : getcolor('0203')})
    args.update({'e0243' : getcolor('0243')})
    


    #SPE Area Lead
    args.update({'e0222' : getcolor('0222')})
    #SPE 2D Engineer
    args.update({'e0257' : getcolor('0257')})
    args.update({'e0235' : getcolor('0235')})
    args.update({'e0205' : getcolor('0205')})

    #PFA
    args.update({'e0253' : getcolor('0253')})
    #PFA Engineer
    args.update({'e0212' : getcolor('0212')})
    args.update({'em022' : getcolor('M022')})
    args.update({'em014' : getcolor('M014')})
    args.update({'e0241' : getcolor('0241')})
    args.update({'e0213' : getcolor('0213')})

   
    #S3D
    args.update({'e0202' : getcolor('0202')})
    args.update({'e0254' : getcolor('0254')})
    #S3D Indirect
    args.update({'e0113' : getcolor('0113')})
    args.update({'e0250' : getcolor('0250')})
    args.update({'e0251' : getcolor('0251')})


    return render(request, 'hrg_tm/attendance2.html', args)
    

def attendance2nh3(request):

    args = {}

    dt=datetime.date.today()

    args.update({'dt' : dt})
    
    
    #NH3 Area Lead
    args.update({'e0204' : getcolor('0204')})
    args.update({'e0207' : getcolor('0207')})
    #NH3 Designer
    args.update({'e0221' : getcolor('0221')})
    args.update({'e0117' : getcolor('0117')})
    args.update({'e0116' : getcolor('0116')})
    #NH3 S3D Designer
    args.update({'e0219' : getcolor('0219')})
    args.update({'e0215' : getcolor('0215')})
    args.update({'e0248' : getcolor('0248')})
    args.update({'e0263' : getcolor('0263')})
    args.update({'e0262' : getcolor('0262')})
    args.update({'e0206' : getcolor('0206')})


    
    return render(request, 'hrg_tm/attendance2nh3.html', args)


def attendance2urea(request):

    args = {}

    dt=datetime.date.today()

    args.update({'dt' : dt})
    
   

    #Urea Area Lead
    args.update({'e0223' : getcolor('0223')})
    #Urea Designer
    args.update({'e0229' : getcolor('0229')})
    args.update({'e0269' : getcolor('0269')})
    #Urea S3D Designer
    args.update({'e0259' : getcolor('0259')})
    args.update({'e0252' : getcolor('0252')})
    args.update({'em032' : getcolor('M032')})
    args.update({'e0258' : getcolor('0258')})


    return render(request, 'hrg_tm/attendance2urea.html', args)


def attendance2utility(request):

    args = {}

    dt=datetime.date.today()

    args.update({'dt' : dt})
    
    


    #Utility Area Lead
    args.update({'e0216' : getcolor('0216')})
    #Utility Designer
    args.update({'em031' : getcolor('M031')})
    args.update({'e0274' : getcolor('0274')})
    #Utility S3D Designer
    args.update({'e0256' : getcolor('0256')})
    args.update({'e0271' : getcolor('0271')})
    args.update({'e0208' : getcolor('0208')})
    args.update({'e0226' : getcolor('0226')})
    args.update({'e0268' : getcolor('0268')})

   

    return render(request, 'hrg_tm/attendance2utility.html', args)
    

def attendance2piperack(request):

    args = {}

    dt=datetime.date.today()

    args.update({'dt' : dt})
    
    #Piperack Area Lead
    args.update({'e0217' : getcolor('0217')})
    #Piperack Designer
    args.update({'e0211' : getcolor('0211')})
    args.update({'e0246' : getcolor('0246')})
    
    #Piperack S3D Designer
    args.update({'e0203' : getcolor('0203')})
    args.update({'e0243' : getcolor('0243')})
   

   

    return render(request, 'hrg_tm/attendance2piperack.html', args)
 

def attendance2spe(request):

    args = {}

    dt=datetime.date.today()

    args.update({'dt' : dt})
    
   #SPE Area Lead
    args.update({'e0222' : getcolor('0222')})
    #SPE 2D Engineer
    args.update({'e0257' : getcolor('0257')})
    args.update({'e0235' : getcolor('0235')})
    args.update({'e0205' : getcolor('0205')})

   
    return render(request, 'hrg_tm/attendance2spe.html', args)


def attendance2pfa(request):

    args = {}

    dt=datetime.date.today()

    args.update({'dt' : dt})
    
   

    #PFA
    args.update({'e0253' : getcolor('0253')})
    #PFA Engineer
    args.update({'e0212' : getcolor('0212')})
    args.update({'em022' : getcolor('M022')})
    args.update({'em014' : getcolor('M014')})
    args.update({'e0241' : getcolor('0241')})
    args.update({'e0213' : getcolor('0213')})

    

    return render(request, 'hrg_tm/attendance2pfa.html', args)
    

def attendance2pid(request):

    args = {}

    dt=datetime.date.today()

    args.update({'dt' : dt})
    
   
    #SPPID
    args.update({'e0238' : getcolor('0238')})
    args.update({'e0244' : getcolor('0244')})

    return render(request, 'hrg_tm/attendance2pid.html', args)
 

def attendance2s3d(request):

    args = {}

    dt=datetime.date.today()

    args.update({'dt' : dt})
    
     #S3D
    args.update({'e0202' : getcolor('0202')})
    args.update({'e0254' : getcolor('0254')})
    #S3D Indirect
    args.update({'e0113' : getcolor('0113')})
    args.update({'e0250' : getcolor('0250')})
    args.update({'e0251' : getcolor('0251')})


    return render(request, 'hrg_tm/attendance2s3d.html', args)


def attendance3(request):

    args = {}

    dt=datetime.date.today()
    
    args.update({'e0209' : getcolor('0209')})  
    args.update({'e0220' : getcolor('0220')})
    args.update({'e0109' : getcolor('0109')})
    args.update({'e0270' : getcolor('0270')})
    args.update({'e0238' : getcolor('0238')})
    args.update({'e0251' : getcolor('0251')})
    args.update({'e0112' : getcolor('0112')})
    args.update({'e0247' : getcolor('0247')})
    args.update({'e0233' : getcolor('0233')})
    args.update({'e0245' : getcolor('0245')})
    args.update({'dt' : dt})
    return render(request,'hrg_tm/attendance3.html',args)


def attendance3project1(request):

    args = {}

    dt=datetime.date.today()

    args.update({'e0109' : getcolor('0109')})
    args.update({'e0209' : getcolor('0209')})
    args.update({'e0238' : getcolor('0238')})
    args.update({'e0251' : getcolor('0251')})
    args.update({'e0220' : getcolor('0220')})
    args.update({'e0247' : getcolor('0247')})
    args.update({'e0233' : getcolor('0233')})
    args.update({'e0245' : getcolor('0245')})
    args.update({'e0271' : getcolor('0271')})
    args.update({'e0212' : getcolor('0212')})
    args.update({'e0201' : getcolor('0201')})
    args.update({'e0231' : getcolor('0231')})
    args.update({'e0249' : getcolor('0249')})
    args.update({'e0273' : getcolor('0273')})
    args.update({'e0268' : getcolor('0268')})
    args.update({'e0232' : getcolor('0232')})
    args.update({'e0270' : getcolor('0270')})
    args.update({'e0112' : getcolor('0112')})

    args.update({'dt' : dt})
    return render(request,'hrg_tm/attendance3project1.html',args)


def attendance3project2(request):

    args = {}

    dt=datetime.date.today()

    args.update({'e0109' : getcolor('0109')})
    args.update({'e0209' : getcolor('0209')})
    args.update({'e0238' : getcolor('0238')})
    args.update({'e0251' : getcolor('0251')})
    args.update({'e0220' : getcolor('0220')})
    args.update({'e0247' : getcolor('0247')})
    args.update({'e0233' : getcolor('0233')})
    args.update({'e0245' : getcolor('0245')})
    args.update({'e0271' : getcolor('0271')})
    args.update({'e0212' : getcolor('0212')})
    args.update({'e0201' : getcolor('0201')})
    args.update({'e0231' : getcolor('0231')})
    args.update({'e0249' : getcolor('0249')})
    args.update({'e0273' : getcolor('0273')})
    args.update({'e0268' : getcolor('0268')})
    args.update({'e0232' : getcolor('0232')})
    args.update({'e0270' : getcolor('0270')})
    args.update({'e0112' : getcolor('0112')})

    args.update({'dt' : dt})
    return render(request,'hrg_tm/attendance3project2.html',args)


def attendance3s3d(request):
    args = {}

    dt=datetime.date.today()

    args.update({'e0109' : getcolor('0109')})
    args.update({'e0209' : getcolor('0209')})
    args.update({'e0238' : getcolor('0238')})
    args.update({'e0251' : getcolor('0251')})
    args.update({'e0220' : getcolor('0220')})
    args.update({'e0247' : getcolor('0247')})
    args.update({'e0233' : getcolor('0233')})
    args.update({'e0245' : getcolor('0245')})
    args.update({'e0271' : getcolor('0271')})
    args.update({'e0212' : getcolor('0212')})
    args.update({'e0201' : getcolor('0201')})
    args.update({'e0231' : getcolor('0231')})
    args.update({'e0249' : getcolor('0249')})
    args.update({'e0273' : getcolor('0273')})
    args.update({'e0268' : getcolor('0268')})
    args.update({'e0232' : getcolor('0232')})
    args.update({'e0270' : getcolor('0270')})
    args.update({'e0112' : getcolor('0112')})

    args.update({'dt' : dt})
    return render(request,'hrg_tm/attendance3s3d.html',args)


def attendance4(request):

    args = {}

    dt=datetime.date.today()
    
    args.update({'e0209' : getcolor('0209')})  
    args.update({'e0201' : getcolor('0201')})
    args.update({'e0109' : getcolor('0109')})
    args.update({'e0270' : getcolor('0270')})
    args.update({'e0238' : getcolor('0238')})
    args.update({'e0251' : getcolor('0251')})
    args.update({'e0112' : getcolor('0112')})
    args.update({'e0247' : getcolor('0247')})
    args.update({'e0233' : getcolor('0233')})
    args.update({'e0245' : getcolor('0245')})
    args.update({'e0231' : getcolor('0231')})
    args.update({'e0232' : getcolor('0232')})
    args.update({'e0249' : getcolor('0249')})
    args.update({'e0273' : getcolor('0273')})
    args.update({'dt' : dt})
    return render(request,'hrg_tm/attendance4.html',args)




def getcolor(id):
    dt=datetime.date.today()
    color = 'red'
    
    if len(transaction_info.objects.filter(employeeid=id).filter(timesheetdate=dt).filter(halfday=1)) != 0:
            if len(transaction_info.objects.get(employeeid=id, timesheetdate=dt, halfday=1).reason) !=0:
                color = 'orange'
    if len(transacations.objects.filter(employeeid=id).filter(timesheetdate=dt).filter(inout=0)) != 0 :
        color = 'green'
    if len(transacations.objects.filter(employeeid=id).filter(timesheetdate=dt).filter(inout=1)) != 0 :          
        color = 'red'
    if len(user_detail.objects.filter(picture=str(id)+'.jpg').filter(remarks='WFH')) != 0 :
        color = 'blue'
    
    return color


def days_between(d1, d2):
    
    return abs(d2-d1).days



def attendance_api(request, word):
    args = {}
    # uname = request.user.last_name +', '+ request.user.first_name
    
    upic = ""
    # if len(user_detail.objects.filter(mhiid=request.user.id)) !=0 :
    #     upic = user_detail.objects.get(mhiid=request.user.id).pictureurl

    

    projcode = tblmaster.objects.raw("SELECT dbo.hrg_hr_ref_projectcode.id, dbo.hrg_hr_ref_projectcode.projectcodedesc FROM dbo.hrg_hr_tblmaster INNER JOIN dbo.hrg_hr_ref_projectcode ON dbo.hrg_hr_tblmaster.projectcode_id = dbo.hrg_hr_ref_projectcode.id WHERE (NOT (dbo.hrg_hr_tblmaster.employeestatus_id IN (3, 4))) GROUP BY dbo.hrg_hr_ref_projectcode.projectcodedesc, dbo.hrg_hr_ref_projectcode.id ORDER BY dbo.hrg_hr_ref_projectcode.projectcodedesc")

    

    wrd=word
    wrd=wrd.replace('attendance/','')
    

    if wrd=='ALL':
    
        empllist = tblmaster.objects.raw("SELECT dbo.hrg_hr_tblmaster.id, dbo.hrg_hr_tblmaster.employeeid, dbo.hrg_hr_tblmaster.nickname, dbo.hrg_hr_tblmaster.dateemployed, dbo.hrg_hr_user_detail.pictureurl , dbo.auth_user.id AS mhiid  FROM dbo.auth_user INNER JOIN dbo.hrg_hr_user_detail ON dbo.auth_user.id = dbo.hrg_hr_user_detail.mhiid_id INNER JOIN dbo.hrg_hr_tblmaster ON dbo.auth_user.username = dbo.hrg_hr_tblmaster.username WHERE (dbo.hrg_hr_tblmaster.employeestatus_id <> 3) ORDER BY dbo.hrg_hr_tblmaster.nickname")

    else:

        empllist = tblmaster.objects.raw("SELECT dbo.hrg_hr_tblmaster.id, dbo.hrg_hr_tblmaster.employeeid, dbo.hrg_hr_tblmaster.nickname, dbo.hrg_hr_tblmaster.dateemployed, dbo.hrg_hr_user_detail.pictureurl , dbo.auth_user.id AS mhiid FROM dbo.auth_user INNER JOIN dbo.hrg_hr_user_detail ON dbo.auth_user.id = dbo.hrg_hr_user_detail.mhiid_id INNER JOIN dbo.hrg_hr_tblmaster ON dbo.auth_user.username = dbo.hrg_hr_tblmaster.username INNER JOIN dbo.hrg_hr_ref_projectcode ON dbo.hrg_hr_tblmaster.projectcode_id = dbo.hrg_hr_ref_projectcode.id WHERE (dbo.hrg_hr_tblmaster.employeestatus_id <> 3) AND (dbo.hrg_hr_ref_projectcode.projectcodedesc = '"+wrd+"') ORDER BY dbo.hrg_hr_tblmaster.nickname")

    attend = []
    color = 'red'
    dt=datetime.date.today()
    
    
    for i in empllist:
        color = 'red'
        

        if len(transaction_info.objects.filter(employeeid=i.employeeid).filter(timesheetdate=dt).filter(halfday=1)) != 0:
            if len(transaction_info.objects.get(employeeid=i.employeeid, timesheetdate=dt, halfday=1).reason) !=0:
                color = 'orange'
                

        if len(transacations.objects.filter(employeeid=i.employeeid).filter(timesheetdate=dt).filter(inout=0)) != 0 :
            color = 'green'
            

        if len(transacations.objects.filter(employeeid=i.employeeid).filter(timesheetdate=dt).filter(inout=1)) != 0 :          
            color = 'red'
            

        if len(user_detail.objects.filter(mhiid_id=i.mhiid).filter(remarks='WFH')) != 0 :
            color = 'blue'

        if len(user_detail.objects.filter(mhiid_id=i.mhiid).filter(remarks='NS')) != 0 :
            color = '#6610f2'
            
        
        if i.dateemployed != 'None':           
            dy = days_between(i.dateemployed,dt)
        else:
            dy= 50
           
        if (dy < 32):
            newemp = 'new'
        else:
            newemp = 'old'

        attend.append([{'id' : i.id},{'nickname' : i.nickname},i.pictureurl,color,newemp])
        args.update({i.nickname : [i.id,i.nickname,i.pictureurl,color]} )
   
        

    return JsonResponse (data=args)
