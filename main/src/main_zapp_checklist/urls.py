
from django.urls import path, include
from . import views

urlpatterns = [
    path('check/<str:mhiid>/', views.index, name='checklist-index'),
    path('report/', views.report, name='checklist-report'),
]