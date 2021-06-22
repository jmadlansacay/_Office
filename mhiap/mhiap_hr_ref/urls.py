from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.mylogin, name='mylogin'),
    path('logout/', views.mylogout, name='mylogout'),
    # path('forbidden/', views.forbidden, name='forbidden')
]