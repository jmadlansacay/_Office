from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('population-chart/<str:word>/', views.population_chart, name='population-chart'),
]
