from django.contrib import admin
from .models import user_detail, UserAccess
# Register your models here.


class user_detailView(admin.ModelAdmin):
    list_display = ('mhi_id', 'last_name', 'first_name', 'nick_name', 'access', 'pic', 'project')
    search_fields = ('mhi_id', 'last_name', 'first_name', 'nick_name',)
    list_filter = ('access', 'project')


admin.site.register(user_detail,user_detailView)
admin.site.register(UserAccess)



