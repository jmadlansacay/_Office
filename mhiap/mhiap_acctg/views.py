from django.shortcuts import render
from mhiap_hr_ref.util import getUserDetail, getPermission
# Create your views here.



def acctg_index(request):
    context = {}
    udetail = getUserDetail(request.user.username)
    context.update({'udetail' : udetail })
    uname = request.user.last_name+', '+request.user.first_name
    context.update({'uname' : uname })
    
    if getPermission(request.user.username,'ACCTG') == 0 :
        context.update({'error' : 'ACCESS DENIED'})
        return render(request,'mhiap_hr/hr_error.html', context)

    return render(request,'mhiap_acctg/index.html', context)