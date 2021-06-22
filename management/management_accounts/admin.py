from django.contrib import admin
from .models import *



class ProjectsView(admin.ModelAdmin):
    list_display = ('project','color')

admin.site.register(Projects)
