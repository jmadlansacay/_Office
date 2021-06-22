from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^hrg_tm/attendance_new/(?P<word>.*)/$', views.attendance_api, name='attendance_new'),
    url(r'^hrg_tm/attendance/(?P<word>.*)/$', views.attendance, name='attendance'),
    url(r'^hrg_tm/details/(?P<pk>\d+)/$', views.attendance_details, name='attendance_details'),
    url(r'^hrg_tm/details/msg/(?P<word>.*)/$', views.msg_update, name='msg_update'),
    url(r'^hrg_tm/attendance2/$', views.attendance2, name='attendance2'),
    url(r'^hrg_tm/attendance2/nh3/$', views.attendance2nh3, name='attendance2nh3'),
    url(r'^hrg_tm/attendance2/urea/$', views.attendance2urea, name='attendance2urea'),
    url(r'^hrg_tm/attendance2/utility/$', views.attendance2utility, name='attendance2utility'),
    url(r'^hrg_tm/attendance2/piperack/$', views.attendance2piperack, name='attendance2piperack'),
    url(r'^hrg_tm/attendance2/spe/$', views.attendance2spe, name='attendance2spe'),
    url(r'^hrg_tm/attendance2/pfa/$', views.attendance2pfa, name='attendance2pfa'),
    url(r'^hrg_tm/attendance2/pid/$', views.attendance2pid, name='attendance2pid'),
    url(r'^hrg_tm/attendance2/s3d/$', views.attendance2s3d, name='attendance2s3d'),
    url(r'^hrg_tm/attendance3/$', views.attendance3, name='attendance3'),
    url(r'^hrg_tm/attendance3/project1/$', views.attendance3project1, name='attendance3project1'),
    url(r'^hrg_tm/attendance3/project2/$', views.attendance3project2, name='attendance3project2'),
    url(r'^hrg_tm/attendance3/s3d/$', views.attendance3s3d, name='attendance3s3d'),
    url(r'^hrg_tm/attendance4/$', views.attendance4, name='attendance4'),
]