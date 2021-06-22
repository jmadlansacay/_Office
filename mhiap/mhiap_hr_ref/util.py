from django.contrib.auth.models import User
from .models import UserDetail



def getUserDetail(uname):
    uid = User.objects.get(username=uname).id  
    
    try:
        udetail = UserDetail.objects.get(user_id=uid)
    except:
        udetail = ""

    return udetail


def getPermission(uname, appname):
    uid = User.objects.get(username=uname).id  
    
    try:
        uaccess = UserDetail.objects.get(user_id=uid).permission
        if '*' in uaccess:
            uaccess=1
        else:
            if appname in uaccess:
                uaccess = 1
            else:
                uaccess = 0
    except:
        uaccess = 0

    return uaccess

