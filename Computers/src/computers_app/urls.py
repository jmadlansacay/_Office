from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('app/sync', views.sync, name='sync'),
    path('table/<str:mdl>', views.table, name='table'),
    path('item/<int:pk>', views.item , name='item'),
    
]