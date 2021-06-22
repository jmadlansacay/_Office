from django.urls import path
from . import views

urlpatterns = [
    path('', views.hr_index.as_view(), name ='hr_index'),
    path('hr_master/', views.hr_master.as_view(), name ='hr_master'),
    path('hr_master/edit/<int:pk>/', views.hr_master_edit, name ='hr_master_edit'),
    path('error/', views.hr_error, name ='hr_error'),
    
]