from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pic = models.ImageField(upload_to ='user/', default='NoManPic.jpg')
    permission = models.CharField(max_length=100, default='USER')

    


class EmployeeTypeCode(models.Model):
    description = models.CharField(max_length=50, null=False, blank=True)
    prefix = models.CharField(max_length=4, null=False, blank= True)

    def __str__(self):
        return self.description 


class EmployeeStatusCode(models.Model):
    description = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.description



class ProjectCode(models.Model):
    description = models.CharField(max_length=150, blank=False, null=False)
    project_name = models.CharField(max_length=150, blank=False, null=False)
    project_supervisor = models.CharField(max_length=50, blank=False, null=False)
    start_date = models.DateField(blank=False, null=False)
    end_date = models.DateField(blank=False, null=False)

    def __str__(self):
        return self.description


class DesignationCode(models.Model):
    description = models.CharField(max_length=150, blank=False, null=False)
    designation_group = models.CharField(max_length=150, blank=False, null=False)
    
    def __str__(self):
        return self.description



