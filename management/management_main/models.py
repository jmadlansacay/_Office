from django.db import models
from management_accounts.models import Projects


class ProjectHours(models.Model):     
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    year = models.IntegerField()
    jan_hrs = models.FloatField(default=0)
    feb_hrs = models.FloatField(default=0)
    mar_hrs = models.FloatField(default=0)
    apr_hrs = models.FloatField(default=0)
    may_hrs = models.FloatField(default=0)
    jun_hrs = models.FloatField(default=0)
    jul_hrs = models.FloatField(default=0)
    aug_hrs = models.FloatField(default=0)
    sep_hrs = models.FloatField(default=0)
    oct_hrs = models.FloatField(default=0)
    nov_hrs = models.FloatField(default=0)
    dec_hrs = models.FloatField(default=0)

    def __str__(self):
        return str(self.project) + ' - ' + str(self.year)

    class Meta:
        unique_together =('project', 'year')
        verbose_name = "No of Project Hour"


class Employees(models.Model):
    employee_idno = models.CharField(max_length=4, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    nickname = models.CharField(max_length=50, blank=True, null=True)
    project = models.ForeignKey(Projects, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return str(self.last_name)+', '+str(self.first_name)

    class Meta:
        verbose_name = "Employee List"
