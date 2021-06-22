
from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    #path('', views.index, name='index'),
    #path('skills/<int:id>/', views.skills_map, name="skills_map"),
    # path('skills/user/<str:wrd>', views.admin_skills_map, name="admin_skills_map"),
    # path('skills/acctg/<str:wrd>', views.acctg_skills_map, name="acctg_skills_map"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('skills_list/', views.skills_list, name="skills_list"),
    path('skillseval/<str:wrd>', views.skills_map, name="skills_map"),
    path('skills_list/export', views.export_users_csv2, name="export_skills"),
    path('comsugg/', views.comsugg, name="comsugg"),
    
]