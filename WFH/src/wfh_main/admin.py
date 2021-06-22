from django.contrib import admin

# Register your models here.
from .models import MainHrHrMaster, MainRefProjectCode, MainAccountsAccountDetails



class MultiDBModelAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        obj.delete(using=self.using)

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        return super().formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)

    def formfield_for_manytomany(self,db_field, request, **kwargs):
        return super().formfield_for_manytomany(db_field, request, using=self.using, **kwargs)

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the user app is involved.
        """
        if obj1._meta.app_label == 'main' or \
           obj2._meta.app_label == 'main':
           return True
        return None

    
class ProfileSectionAdmin(MultiDBModelAdmin):
    using = 'main'
 

admin.site.register(MainHrHrMaster, ProfileSectionAdmin)
admin.site.register(MainRefProjectCode, ProfileSectionAdmin)
admin.site.register(MainAccountsAccountDetails, ProfileSectionAdmin)




