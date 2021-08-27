
from django.urls import path, include
from . import views


urlpatterns = [
    path('error/',views.error,name='eval-error'),
    path('accessdenied/',views.AccessDenied,name='eval-AccessDenied'),
    path('sync/',views.HrSync,name='eval-HrSync'),
    path('',views.index,name='eval-index'),
    path('myevaluation/', views.MyEvaluation, name='eval-MyEvaluation'),
    path('evaluation/', views.EvaluationList, name='eval-Evaluation'),
    path('evaluation/<str:idno>', views.EvaluationLead, name='eval-EvaluationLead'),
    path('myskills/', views.MySkills, name='eval-MySkills'),
    path('skills/', views.SkillList, name='eval-Skills'),
    path('skills/<str:idno>', views.SkillLead, name='eval-SkillLead'),
    path('skills_export/export', views.export_users_csv2, name="export_skills"),
    path('mycomments/', views.MyComments, name='eval-MyComments'),
    path('comments/', views.CommentsList, name='eval-Comments'),
    path('comments/<str:idno>', views.CommentLead, name='eval-CommentLead'),
    path('excel/<str:idno>', views.WriteToExcel, name='eval-WriteToExcel'),
    path('commentspdf/', views.CommentsPDF, name='eval-CommentsPDF')
    
]
