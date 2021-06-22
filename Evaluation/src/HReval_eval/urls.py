
from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('', views.index, name='index'),
    path('evaluation/<int:id>/', views.evaluation, name="evaluation"),
    path('login/', views.mylogin, name='mylogin'),
    path("logout/", views.mylogout, name="mylogout"),
    path('changepass/', views.change_password, name='change_password'),
    path('regular/<str:wrd>', views.regular_emp, name='regular_emp'),
    path('error/', views.error_msg, name='error'),
    url('export/csv/', views.export_users_csv, name='export_users_csv'),
    path('performance/', views.performance, name='performance'),
    
]