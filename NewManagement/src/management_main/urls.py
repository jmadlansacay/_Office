from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name='main-index'),
    path('<int:id>/', views.covidoverview, name='covidoverview'),
    path('<int:id>/', views.news_events_photos, name='news_events_photos'),
    path('news_events_photos/<int:id>/', views.news_events_photos, name='news_events_photos'),
    path('managers/<int:id>/', views.messages_managers, name='messages_managers'),
    path('manhours/', views.manhours, name='manhours'),
    path('employeemanhours/', views.employeemanhours, name='employeemanhours'),
    path('employees/<str:wrd>/', views.employees, name='main-employees'),
    path('message/', views.message, name='message'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

