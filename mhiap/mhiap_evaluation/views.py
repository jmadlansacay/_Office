from django.shortcuts import render
from mhiap_hr.models import HrMaster
from django.db.models import Q
# Create your views here.
def eval_index(request):
    context = {}
    hr = HrMaster.objects.filter(Q(employee_status=2)|Q(employee_status=1)|Q(employee_status=5)|Q(employee_status=7))
    context.update({'hr':hr})

    return render(request, 'mhiap_evaluation/index.html', context)