from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.mylogin, name='mylogin'),
    url(r'^logout/$', views.mylogout, name='mylogout'),
    url(r'^hrg_hr/users_list/$', views.users_list, name='users_list'),
    url(r'^password/$', views.change_password, name='change_password'),
    url(r'^hrg_hr/add/$', views.users_add, name='users_add'),
    url(r'^hrg_hr/users_detail/(?P<pk>\d+)/$', views.users_detail, name='users_detail'),
    url(r'^hrg_hr/users_delete/(?P<pk>\d+)/$', views.users_delete, name='users_delete'),

    #url(r'^settings/site$', views.settings_site, name='settings_site'),

    #url(r'^attendance/(?P<word>.*)/$', views.attendance, name='attendance'),
    #url(r'^login/$', views.mylogin, name='mylogin'),
    #url(r'^logout/$', views.mylogout, name='mylogout'),
    #url(r'^accounts/', include('django.contrib.auth.urls')),
    #url(r'^attendance/(?P<word>.*)/$', views.attendance, name='attendance'),
    #url(r'^hrg_hr/users_list/$', views.error404, name='error404'),
    #url(r'^forbidden/$', views.forbidden, name='forbidden'),
    #url(r'^permission/$', views.permission, name='permission'),
    #url(r'^hrmaster/add/$', views.hrmaster_add, name='hrmaster_add'),
    #url(r'^news/(?P<word>.*)/$', views.news_detail, name='news_detail'),
]