from django.db import models

# Create your models here.
class gendercode(models.Model):
    genderdescription = models.CharField(max_length=10)  

    def __str__(self):
        return self.genderdescription


class employeestatuscode(models.Model):
    employeestatusdescription = models.CharField(max_length=20)  

    def __str__(self):
        return self.employeestatusdescription



class projectcode(models.Model):
    projectcode = models.CharField(max_length=3)  # Field name made lowercase.
    projectcodedesc = models.CharField(max_length=50, blank=True, null=True)  # Field name made lowercase.
    projectname = models.TextField(blank=True, null=True)  # Field name made lowercase.
    projectsupervisor = models.CharField(max_length=50, blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateField(blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(blank=True, null=True)  # Field name made lowercase.
    isactive = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    multicharge = models.IntegerField(blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return str(self.projectcodedesc) 