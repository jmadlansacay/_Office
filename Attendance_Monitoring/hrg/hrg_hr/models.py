from django.contrib.auth.models import User
from django.db import models
from hrg_hr_ref.models import *


# Create your models here.
class user_detail(models.Model):
    mhiid = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.CharField(max_length=50, blank=True, null=True)
    pictureurl = models.CharField(max_length=150, blank=True, null=True)
    user_access = models.CharField(max_length=20, blank=True, null=True)
    remarks =  models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.mhiid) +' - ' +str(self.picture)+' - '+str(self.mhiid.last_name)+', '+str(self.mhiid.first_name)


class tblmaster(models.Model):
    username = models.CharField(max_length=150,blank=True, null=True) 
    employeeid = models.CharField(max_length=4)  
    employeetype = models.CharField(max_length=2)  
    lastname = models.CharField(max_length=50, blank=True, null=True)  
    firstname = models.CharField(max_length=50, blank=True, null=True)  
    middlename = models.CharField(max_length=50, blank=True, null=True)  
    nickname = models.CharField(max_length=50, blank=True, null=True)  
    employeestatus = models.ForeignKey(employeestatuscode, blank=True, null=True, on_delete=models.CASCADE)  
    gender = models.ForeignKey(gendercode, blank=True, null=True, on_delete=models.CASCADE)  
    civilstatus = models.IntegerField(blank=True, null=True)  
    dateofbirth = models.DateField(blank=True, null=True)  
    birthplace = models.CharField(max_length=50, blank=True, null=True)  
    sssno = models.CharField(max_length=12, blank=True, null=True)  
    tin = models.CharField(max_length=11, blank=True, null=True)  
    philhealthno = models.CharField(max_length=14, blank=True, null=True)  
    pagibigno = models.CharField(max_length=14, blank=True, null=True)  
    picture = models.CharField(max_length=50, blank=True, null=True)  
    designation = models.CharField(max_length=2, blank=True, null=True)  
    dateemployed = models.DateField(blank=True, null=True)  
    dateresigned = models.DateField(blank=True, null=True)  
    shiftcode = models.CharField(max_length=2, blank=True, null=True)  
    projectcode = models.ForeignKey(projectcode, blank=True, null=True, on_delete=models.CASCADE) 
    height = models.FloatField(blank=True, null=True)  
    weight = models.FloatField(blank=True, null=True)  
    basic = models.FloatField(blank=True, null=True)  
    effectivitydate = models.DateField(blank=True, null=True)  
    deminimis = models.FloatField(blank=True, null=True)  
    fringe = models.FloatField(blank=True, null=True)  
    leavecredits = models.FloatField(blank=True, null=True)  
    slcredits = models.FloatField(blank=True, null=True)  
    vlcredits = models.FloatField(blank=True, null=True)  
    taxcode = models.CharField(max_length=50, blank=True, null=True)  
    philhealth = models.FloatField(blank=True, null=True)  
    oldbasic = models.FloatField(blank=True, null=True)  
    isict = models.IntegerField(blank=True, null=True)  

    def __str__(self):
        return str(self.username) +' - ' +str(self.lastname)+', '+str(self.firstname)+' - ' +str(self.employeeid)



class intro(models.Model):
    employeeid = models.CharField(max_length=4, blank=True, null=True)
    msg = models.TextField(blank=True)

    def __str__(self):
        return str(self.employeeid)