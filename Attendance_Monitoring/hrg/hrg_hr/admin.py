from django.contrib import admin
from .models import user_detail, tblmaster, intro

# Register your models here.
class user_detailView(admin.ModelAdmin):
    list_display=('mhiid','lastname','firstname','remarks',)
    search_fields =('mhiid__last_name','mhiid__first_name','mhiid__username','remarks',)

    def lastname(self,obj):
        return obj.mhiid.last_name
    
    def firstname(self,obj):
        return obj.mhiid.first_name


admin.site.register(user_detail,user_detailView)


class tblmasterView(admin.ModelAdmin):
    list_display=('username', 'lastname', 'firstname', 'nickname', 'employeestatus','projectcode','dateemployed')
    search_fields = ('username', 'lastname', 'firstname', 'nickname')
    list_filter =('employeestatus', 'projectcode')


     


admin.site.register(tblmaster, tblmasterView)
admin.site.register(intro)