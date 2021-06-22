from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main-index'),
    path('employees/<str:wrd>/', views.employees, name='main-employees')
    
]
