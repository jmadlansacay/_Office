from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(ComputerModel)
admin.site.register(ItemType)
admin.site.register(UserNames)



class computer_inventoryView(admin.ModelAdmin):

    def item_type(self,obj):
        return obj.item_model.item_type

    list_display = ('item_code','item_type','item_model','device_name','serial_number', 'item_status', 'item_user')
    search_fields = ('item_code', 'item_model__item_type','item_model__model_description', 'device_name', 'serial_number', 'item_user__nick_name')
    list_filter = ('item_model','item_status')

admin.site.register(computer_inventory,computer_inventoryView)