from django.shortcuts import render
from django.http import JsonResponse
from . models import *
import json
# Create your views here.
def api_test(request, pj):
    
    dt = ref_user_access.objects.filter()

    context={}
    for i in dt:
        context.update({i.user_access_description : i.sort_order})
    
    return JsonResponse(data=context)




    # ref_user_access(models.Model):
    # user_access_description = models.CharField(max_length=20, blank=True, null=True)
    # sort_order = models.IntegerField(default=0)