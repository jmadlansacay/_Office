
from django.urls import path
from . import views

urlpatterns = [
    path('custom/', views.customform, name='custom_form'),
    path('list/', views.listform, name='list_form'),
    path('custom/edit/<int:pk>', views.editform, name='edit_form'),
]
