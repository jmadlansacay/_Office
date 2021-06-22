from django.urls import path
from .import views

urlpatterns = [
    path('dashboard/', views.dashboard , name='ims-dashboard'),
    path('dashboard/getpic/<str:icn>', views.geticninfo, name='ims-getpic'),
    path('charts/location/', views.location_chart , name='ims-location_chart'),
    path('charts/area/', views.area_chart , name='ims-area_chart'),
    path('icn/change_location/<str:icn>/<str:uname>', views.change_location , name='ims-change_location'),
    path('modal/', views.modal, name='modal')
]
