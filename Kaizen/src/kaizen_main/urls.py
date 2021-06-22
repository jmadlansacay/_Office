from django.urls import path
from . import views


urlpatterns = [
    path('1/',views.part1, name='part1'),
    path('2/',views.part2, name='part2'),
]