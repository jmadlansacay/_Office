
from django.urls import path

from . import views

urlpatterns = [
    
    path('pdf/', views.topdf , name='topdf'),
]