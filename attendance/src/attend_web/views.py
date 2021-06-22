from django.shortcuts import render
from attend_main.models import MainAccountsAccountDetails
from attend.Util import getuserdetail
from .models import *
# Create your views here.
def index(request):

    context = {}
    a = getuserdetail(request)
    # print(a['uid'])
    # print(a['uname'])
    J = MainAccountsAccountDetails.objects.using('main').get(mhi_id='U298835').access
    print(J)

    if a =='':
        context.update({'msg' : 'Invalid User'})
        return render(request,'attend_web/error.html', context)
    
    
    if len(access.objects.filter(mhi_id=a['uid'])) == 0:
        context.update({'msg' : 'Access Denied'})
        return render(request,'attend_web/error.html', context)

    return render(request,'attend_web/index.html', context)
