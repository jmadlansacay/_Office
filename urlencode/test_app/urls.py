from django.urls import path
from . import views
urlpatterns = [
    
    path('test/<enc:wrd>', views.index)
]
