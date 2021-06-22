from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import user_detail
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
import smtplib


# Create your views here.

def mylogin(request):
    
    if request.method == 'POST' :

        utxt = request.POST.get('username')
        ptxt = request.POST.get('password')

        if utxt != "" and ptxt != "" :
            user = authenticate(username=utxt, password=ptxt)
            
            if user != None :
                login(request, user)
                
                return redirect('index')

    return render(request, 'hrg_hr/login.html')



def mylogout(request):

    logout(request)

    return redirect('mylogin')



def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('index')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'hrg_hr/change_password.html', {'form': form})




def index(request):

    return redirect('attendance', word='ALL')

    # args = {}
    # uname = request.user.last_name +', '+ request.user.first_name
    # args.update({'uname' : uname})
    # upic = "/media/NoPicMan.jpg"
    # if len(user_detail.objects.filter(mhiid=request.user.id)) !=0 :
    #     upic = user_detail.objects.get(mhiid=request.user.id).pictureurl

    # args.update({'upic' : upic})
   

    # if user_detail.objects.get(mhiid=request.user.id).user_access == 'ATTENDANCE' or user_detail.objects.get(mhiid=request.user.id).user_access == 'USER' or user_detail.objects.get(mhiid=request.user.id).user_access == 'ATTENDANCE_ADMIN':
        
    #     return redirect('attendance', word='ALL')

    

    # return render (request, 'hrg_hr/index.html',args)




def users_list(request):

    args = {}
    uname = request.user.last_name +', '+ request.user.first_name
    args.update({'uname' : uname})
    upic = ""
    if len(user_detail.objects.filter(mhiid=request.user.id)) !=0 :
        upic = user_detail.objects.get(mhiid=request.user.id).pictureurl

    args.update({'upic' : upic})

    #ulist = User.objects.all()
    ulist = User.objects.raw("SELECT dbo.auth_user.id, dbo.auth_user.username, dbo.auth_user.first_name, dbo.auth_user.last_name, dbo.auth_user.email, dbo.hrg_hr_user_detail.picture, dbo.hrg_hr_user_detail.pictureurl FROM dbo.auth_user LEFT OUTER JOIN dbo.hrg_hr_user_detail ON dbo.auth_user.id = dbo.hrg_hr_user_detail.mhiid_id")

    args.update({'ulist' : ulist})

    return render (request, 'hrg_hr/users_list.html', args)




def users_add(request):

    args = {}
    uname = request.user.last_name +', '+ request.user.first_name
    args.update({'uname' : uname})
    upic = ""
    if len(user_detail.objects.filter(mhiid=request.user.id)) !=0 :
        upic = user_detail.objects.get(mhiid=request.user.id).pictureurl

    args.update({'upic' : upic})

    
    if request.method == "POST" :

        uname = request.POST.get('username')
        lname = request.POST.get('last_name')
        fname = request.POST.get('first_name')
        email = request.POST.get('email')

       

        myfile = request.FILES['myfile']
        fs = FileSystemStorage()

        filename = fs.save(myfile.name, myfile)
        url = fs.url(filename)

        
        if str(myfile.content_type).startswith("image"):

            if uname=="" or lname=="" or fname=="" or email=="" :
                fs = FileSystemStorage()
                fs.delete(filename)

                error = "Fields should not be empty"
                return render(request, 'hrg_hr/error404.html' , {'error':error})


            b=User(username=uname, email=email, last_name=lname, first_name=fname)
            b.save()
            mhiid = User.objects.get(username=uname).id
            u = user_detail(mhiid_id=mhiid, picture = filename, pictureurl=url)
            u.save()

            return redirect('users_list')
        else:

            fs = FileSystemStorage()
            fs.delete(filename)

            error = "Your File Not Supported"
            return render(request, 'hrg_hr/error404.html' , {'error':error})

    return render (request, 'hrg_hr/users_add.html', args)





def users_detail(request,pk):

    args = {}
    uname = request.user.last_name +', '+ request.user.first_name
    args.update({'uname' : uname})
    upic = ""
    if len(user_detail.objects.filter(mhiid=request.user.id)) !=0 :
        upic = user_detail.objects.get(mhiid=request.user.id).pictureurl

    args.update({'upic' : upic})

    if len(User.objects.filter(pk=pk)) == 0 :
        error = "User Not Found"
        return render(request, 'hrg_hr/error404.html' , {'error':error})


    ulist = User.objects.get(pk=pk)
    
    if len(user_detail.objects.filter(mhiid=pk)) == 0 :
        udetail =[]
    else:
        udetail = user_detail.objects.get(mhiid=pk)

    args.update({'ulist' : ulist})
    args.update({'udetail' : udetail})

    return render (request, 'hrg_hr/users_detail.html', args)



def users_delete(request,pk):

    b = User.objects.get(pk=pk)
    

    if len(user_detail.objects.filter(mhiid=pk)) != 0:
        u = user_detail.objects.get(mhiid=pk)
        fs = FileSystemStorage()
        fs.delete(u.picture)
        u.delete()

    b.delete()
    

    return redirect ('users_list')