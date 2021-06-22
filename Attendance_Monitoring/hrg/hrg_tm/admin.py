from django.contrib import admin
from .models import transacations, transaction_info

# Register your models here.
admin.site.register(transacations)
admin.site.register(transaction_info)
