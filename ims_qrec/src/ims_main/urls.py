from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='ims-dashboard'),
    path('error/', views.error, name='ims_main-error'),
    path('dashboard/getpic/<str:icn>', views.geticninfo, name='ims-getpic'),
    path('icn/change_location/<str:icn>/<str:uname>', views.change_location , name='ims-change_location'),
] 