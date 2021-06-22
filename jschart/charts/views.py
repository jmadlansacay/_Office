#view.py
from django.shortcuts import render
from django.db.models import Sum
from django.http import JsonResponse
from .models import City
 
def home(request):
    city = City.objects.all()
    return render(request, 'charts/home.html', {"city" : city})
 
def population_chart(request, word):
    labels = []
    data = []
 
    # queryset = City.objects.values('name').annotate(population=Sum('population')).order_by('-population') 
    if word == 'All':
        queryset = City.objects.filter()
    else:
        queryset = City.objects.filter(name=word)    
    
    
    for entry in queryset:
        labels.append(entry.name)
        data.append(entry.population)
    

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })