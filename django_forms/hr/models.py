from django.db import models
import datetime

# Create your models here.
class CivilStatusCode(models.Model):
    civilstatus = models.CharField(max_length=15, blank=True, null=True) 

    def __str__(self):
        return str(self.civilstatus)



class GenderCode(models.Model):
    gender = models.CharField(max_length=15, blank=True, null=True) 

    def __str__(self):
        return str(self.gender)


class EmployeeStatusCode(models.Model):
    employeestatus = models.CharField(max_length=15, blank=True, null=True) 

    def __str__(self):
        return str(self.employeestatus)



class EmployeeTypeCode(models.Model):
    employeetype = models.CharField(max_length=50, blank=True, null=True)
    prefix = models.CharField(max_length=5, blank=True, null=True) 

    def __str__(self):
        return str(self.employeetype)+ ' - ' + str(self.prefix)


class ProjectCode(models.Model):
    project_description = models.CharField(max_length=50, blank=False, null = False)
    projectname = models.TextField(blank=False, null=False)  
    projectsupervisor = models.CharField(max_length=50, blank=True, null=True)  
    startdate = models.DateField(blank=True, null=True)  
    enddate = models.DateField(blank=True, null=True)  
    isactive = models.IntegerField(blank=True, null=True)  

    def __str__(self):
        return str(self.projectname) 



class HrMaster(models.Model):
    employee_id = models.CharField(max_length=4, blank=False, null= False, unique=True)
    employee_type = models.ForeignKey(EmployeeTypeCode, on_delete=models.DO_NOTHING)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    first_name = models.CharField(max_length=30, blank=False, null=False)
    middle_name = models.CharField(max_length=30, blank=False, null=False)
    employee_status = models.ForeignKey(EmployeeStatusCode, on_delete=models.DO_NOTHING)
    gender =  models.ForeignKey(GenderCode, on_delete=models.DO_NOTHING)
    project =  models.ForeignKey(ProjectCode, on_delete=models.DO_NOTHING)
    civil_status =  models.ForeignKey(CivilStatusCode, on_delete=models.DO_NOTHING)
    date_of_birth = models.DateField(default=datetime.date.today)

    def __str__(self):
        return str(self.last_name)+', '+str(self.first_name)