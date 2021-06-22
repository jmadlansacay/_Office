from django.contrib import admin
from . models import PayrollPeriodReg, StandardRegister
# Register your models here.


class PayrollPeriodRegView(admin.ModelAdmin):
    list_display=('paystart', 'payend', 'modifiedby', 'modifieddate','payperiodtype')


admin.site.register(PayrollPeriodReg, PayrollPeriodRegView)


# class StandardRegisterView(admin.ModelAdmin):
    

admin.site.register(StandardRegister)
