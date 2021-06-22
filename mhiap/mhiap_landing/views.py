from django.shortcuts import render

# Create your views here.
def landing_index(request):
    return render(request, 'mhiap_landing/index.html')