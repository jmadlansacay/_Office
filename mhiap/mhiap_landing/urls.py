from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_index, name ='landing_index'),
    
]