
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('error/',views.error,name='error'),
    path('hrsync/', views.HrSync, name='hrsync'),
    path('attendance/<str:proj>',views.attendance_api, name='attendance_api'),
    path('attendance_details/<str:idno>',views.attendance_details, name='attendance_details'),
]