from django.shortcuts import render
from .forms import HrMasterStyled
# Create your views here.
def ims(request):
    form = HrMasterStyled()

    if request.method =='POST':     
        form =HrMasterStyled(request.POST or None)
        if form.is_valid():
            form.save()

    context = {'form' : form }
    return render(request,'ims/ims.html', context)