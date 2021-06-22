from django.urls import path
from . import views

urlpatterns = [
   path('api_main/<str:pj>', views.api_test, name='test')
    
]