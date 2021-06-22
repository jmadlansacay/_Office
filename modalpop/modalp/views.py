from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
# Create your views here.
def newsignup(request):
    if request.method=="POST":
        if request.POST.get('password1')==request.POST.get('password2'):
            try:
                saveuser=User.objects.create_user(request.POST.get('username'), password=request.POST.get('password1'))
                saveuser.save()
                return render(request,'modalp/index.html',{"form" : UserCreationForm(), "info":"Username "+request.POST.get('username')+ " Created" })
            except IntegrityError:
                return render(request,'modalp/index.html',{"form" : UserCreationForm(), "error":"User already exist" })    
        else:
            return render(request,'modalp/index.html',{"form" : UserCreationForm(), "error":"Password not matching" })

    else:
        return render(request,'modalp/index.html',{"form" : UserCreationForm })