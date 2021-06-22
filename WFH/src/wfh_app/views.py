from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'wfh_app\index.html')


def error(request):
    return render(request, 'wfh_app\error.html')