from django.contrib import admin
from .models import *
# Register your models here.

# class user_detailView(admin.ModelAdmin):
    
#     def employee_name(self, obj):
#         return obj.username.last_name+', '+obj.username.first_name

#     list_display = ('username', 'user_access', 'employee_name', 'pic', 'id')
#     list_filter = ['user_access',]
#     search_fields=('username__last_name', 'username__first_name', 'username__username')


# admin.site.register(models.user_detail, user_detailView)

class hr_masterView(admin.ModelAdmin):
    list_display = ('idno', 'mhi_id','last_name', 'first_name', 'middle_name', 'nick_name','project','gender','employee_status')
    search_fields = ('idno', 'mhi_id','last_name', 'first_name', 'middle_name', 'nick_name')
    list_filter = ('employee_status','gender','project')

admin.site.register(hr_master,hr_masterView)
