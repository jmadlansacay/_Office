from django.contrib import admin
from . import models

# Register your models here.


class ref_user_accessView(admin.ModelAdmin):
    list_display = ('id','user_access_description')

admin.site.register(models.ref_user_access, ref_user_accessView)

class user_detailView(admin.ModelAdmin):

    def employee_name(self, obj):
        return obj.username.last_name+', '+obj.username.first_name

    list_display = ('username', 'user_access', 'employee_name', 'pic', 'id')
    list_filter = ['user_access',]
    search_fields=('username__last_name', 'username__first_name', 'username__username')


admin.site.register(models.user_detail, user_detailView)
admin.site.register(models.ref_unit)


admin.site.register(models.ref_mhi_status)




class ref_areaView(admin.ModelAdmin):
    list_display =('area', 'unit')
    list_filter = ['unit',]

admin.site.register(models.ref_area, ref_areaView)


class tbl_note1View(admin.ModelAdmin):
    list_display = ('icn','rev0','rev1','rev2','rev3','rev4','rev5','rev6')
    search_fields=('icn__area','icn__line_id','rev0','rev1','rev2','rev3','rev4','rev5','rev6')
    list_filter = ['rev0','rev1','rev2','rev3','rev4','rev5','rev6']

admin.site.register(models.tbl_note1,tbl_note1View)




class tbl_icnView(admin.ModelAdmin):
    list_display =('unit','area', 'line_id','location','designer','pid_checker','spe_checker','checker','area_lead','mhi_sv','mhi_status')
    list_filter = ['mhi_status','area_lead', 'checker', 'designer','location']

admin.site.register(models.tbl_icn,tbl_icnView)
admin.site.register(models.ref_hold)

admin.site.register(models.tbl_note2)

admin.site.register(models.ims_settings)