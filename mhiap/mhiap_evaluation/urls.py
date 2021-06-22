from django.urls import path
from . import views

urlpatterns = [
    path('', views.eval_index, name ='eval_index'),
    
    
]