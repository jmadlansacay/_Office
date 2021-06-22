from django.urls import path
from . import views

urlpatterns = [
    path('', views.acctg_index, name ='acctg_index'),
]