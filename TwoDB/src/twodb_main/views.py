from django.shortcuts import render
from .models import HrgHrTblmaster
# Create your views here.
def index(request):

    
    # a = HrgHrTblmaster.objects.all().using('hr')

    # for i in a:
    #     print(i.username)

    return render(request,'twodb_main/index.html')