from django.contrib import admin
from . import models
# Register your models here.

class ref_user_accessView(admin.ModelAdmin):
    list_display = ('id','user_access_description')

admin.site.register(models.ref_user_access, ref_user_accessView)


class user_detailView(admin.ModelAdmin):
    
    list_display = ('username', 'user_access', 'last_name', 'first_name', 'middle_name', 'nickname', 'pic', 'id')
    list_filter = ['user_access',]
    search_fields=('last_name', 'first_name', 'nickname', 'username')


admin.site.register(models.user_detail, user_detailView)
admin.site.register(models.ref_unit)


class ref_areaView(admin.ModelAdmin):
    list_display =('area', 'unit')
    list_filter = ['unit',]

admin.site.register(models.ref_area, ref_areaView)

admin.site.register(models.ref_mhi_status)


class tbl_icnView(admin.ModelAdmin):
    list_display =('unit','area', 'line_id','location','designer','pid_checker','spe_checker','checker','area_lead','mhi_sv','mhi_status')
    list_filter = ['mhi_status','area_lead', 'checker', 'designer','location']

admin.site.register(models.tbl_icn,tbl_icnView)