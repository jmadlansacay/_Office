from django.shortcuts import render
from .forms import HrMasterForm

# Create your views here.
def index(request):
    form = HrMasterForm()

    if request.method =='POST':     
        form =HrMasterForm(request.POST or None)
        if form.is_valid():
            form.save()

    context = {'form' : form }
    return render(request,'hr/index.html', context)
