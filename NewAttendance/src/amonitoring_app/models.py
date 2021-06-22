from django.db import models

# Create your models here.


class transacations(models.Model):
    employeeid = models.CharField(max_length=4, blank=True, null=True)  
    employeetype = models.CharField(max_length=2, blank=True, null=True)  
    timesheetdate = models.DateField(blank=True, null=True)  
    inout = models.IntegerField(blank=True, null=True)  
    timepunch = models.TimeField(blank=True, null=True)  
    createdby = models.CharField(max_length=50, blank=True, null=True)  
    createddate = models.DateTimeField(blank=True, null=True)  
    machinename = models.CharField(max_length=50, blank=True, null=True)  

    def __str__(self):
        return str(self.employeeid) +' - ' +str(self.timesheetdate)+ ' '+ str(self.inout)



class transaction_info(models.Model):
    employeeid = models.CharField(max_length=4, blank=True, null=True)  
    timesheetdate = models.DateField(blank=True, null=True) 
    halfday = models.IntegerField(blank=True, null=True)
    reason = models.CharField(max_length=150, blank=True, null=True)  

    def __str__(self):
        return str(self.employeeid) +' - ' +str(self.timesheetdate)+ ' '+ str(self.halfday)+ ' '+ str(self.reason)
