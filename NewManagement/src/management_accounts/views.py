from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'management_accounts/login.html')