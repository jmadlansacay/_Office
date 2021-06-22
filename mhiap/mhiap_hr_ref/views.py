from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout



# Create your views here.
def mylogin(request):
    
    state = ""
    if request.method == 'POST' :

        utxt = request.POST.get('username')
        ptxt = request.POST.get('password')

        if utxt != "" and ptxt != "" :
            user = authenticate(username=utxt, password=ptxt)
            
            if user != None :
                if user.is_active:
                    login(request, user)
                    if 'next' in request.POST:
                        return redirect(request.POST.get('next'))
                    return redirect('landing_index')
            else:
                state = "Invalid Username/Password !!!!!"
    
    context = {
        'state' : state
        }
    print(state)
    return render(request, 'mhiap_hr_ref/login.html', context)



def mylogout(request):

    logout(request)

    return redirect('landing_index')
# Create your views here.
