from django.contrib import admin
from .models import transacations, transaction_info, access
# Register your models here.
admin.site.register(transacations)
admin.site.register(transaction_info)


admin.site.register(access)