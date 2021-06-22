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


class account_detailsView(admin.ModelAdmin):
    list_display=('mhi_id', 'last_name','first_name','access')
    search_fields=('mhi_id', 'last_name','first_name','access')


admin.site.register(account_details,account_detailsView)

