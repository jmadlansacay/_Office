from django.shortcuts import render
from .models import student
# Create your views here.


def index(request, wrd):

    return render(request,'test.html')
