from django.db import models
from management_accounts.models import Projects
from datetime import date, datetime



class HeadCount(models.Model):

    date = models.DateField(default=date.today)
    source_file = models.ImageField(upload_to='static\management_main\img', height_field=None, width_field=None, max_length=100, blank=True, null=True, default='static\management_main\img\default.jpg')

    def __str__(self):
        return str(self.date)
    
    class Meta:
        verbose_name_plural = "Head Count source file"

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
        verbose_name_plural = "No of Project Hours"


class Employees(models.Model):

    NATIONALITY =[
        ('1', 'FILIPINO'),
        ('2', 'JAPANESE'),
    ]

    EMP_STAT =[
        ('1', 'REGULAR PERMANENT'),
        ('2', 'PROJECT BASE'),
        ('3', 'FIXED TERM'),
        ('4', 'CONSULTANT'),
        ('5', 'REGULAR AP REP'),
        ('6', 'PROBATIONARY'),
        ('7', 'OUTSOURCED'),
        ('8', 'IN-ACTIVE'),
    ]

    EMP_TYPE =[
        ('1', 'EMPLOYEE'),
        ('2', 'NON-EMPLOYEE'),
        ('3', 'DIRECT OUTSOURCED'),
        ('4', 'INDIRECT OUTSOURCED'),
    ]

    PROJ_TYPE =[
        ('1', 'DESIGNER'),
        ('2', 'PROJECT ASSISTANT'),
        ('3', 'COMMON'),
    ]



    last_name = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    nickname = models.CharField(max_length=50, blank=True, null=True)
    project = models.ForeignKey(Projects, on_delete=models.SET_NULL, null=True)
    project_type =models.CharField(max_length=30, choices=PROJ_TYPE, blank=True, null=True)
    nationality = models.CharField(max_length=10, choices=NATIONALITY, blank=True, null=True)
    employee_status = models.CharField(max_length=30, choices=EMP_STAT, blank=True, null=True)
    employee_type = models.CharField(max_length=30, choices=EMP_TYPE, blank=True, null=True)
    remarks = models.CharField(max_length=50, blank=True, null=True)

    
    def __str__(self):
        return str(self.last_name)+', '+str(self.first_name)+' ('+str(self.nickname)+ ')'

    class Meta:
        verbose_name_plural = "Employee List"

class EmployeeHours(models.Model):
    employee = models.ForeignKey(Employees, on_delete=models.DO_NOTHING)
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
        return str(self.employee) + ' - ' + str(self.year)

    class Meta:
        unique_together =('employee', 'year')
        verbose_name_plural = "No of Employee Man Hours"


class Covid(models.Model):

    date = models.DateField(default=date.today)
    total_cases = models.IntegerField(default=0)
    active_cases = models.IntegerField(default=0)
    recovered = models.IntegerField(default=0)
    died = models.IntegerField(default=0)
    bed_occpuancy = models.FloatField(default=0)
    bed_occ = models.IntegerField(default=0)
    bed_vac = models.IntegerField(default=0)
    icu_occ = models.IntegerField(default=0)
    icu_vac = models.IntegerField(default=0)
    isolation_occ = models.IntegerField(default=0)
    isolation_vac = models.IntegerField(default=0)
    ward_occ = models.IntegerField(default=0)
    ward_vac = models.IntegerField(default=0)
    ventilator_occ = models.IntegerField(default=0)
    ventilator_vac = models.IntegerField(default=0)
    daily_cases = models.ImageField(upload_to='static\management_main\img', height_field=None, width_field=None, max_length=100, blank=True, null=True, default='static\management_main\img\default.jpg')
    bed_capacity = models.ImageField(upload_to='static\management_main\img', height_field=None, width_field=None, max_length=100, blank=True, null=True, default='static\management_main\img\default.jpg')

    class Meta:
        db_table="Covid"
        verbose_name_plural = "Covid Tracker"

    def __str__(self):
        return str(self.date)


class Events(models.Model):

    date = models.DateField(default=date.today)
    title = models.CharField(max_length=300, blank=True, null=True)
    body = models.TextField(blank=True)
    pic = models.ImageField(upload_to='static/media/', height_field=None, width_field=None, max_length=100)

    def __str__(self):
        return str(self.title)+ ' ' +str(self.date)

    class Meta:
        verbose_name_plural = "News, Events and Photos"
    
class Financial(models.Model):

    date = models.DateField(default=date.today)
    title = models.CharField(max_length=100, blank=True, null=True)
    pic = models.ImageField(upload_to='static/media/', height_field=None, width_field=None, max_length=100)

    def __str__(self):
        return str(self.date)+ ' ' +str(self.title)

    class Meta:
        verbose_name_plural = "Financial Status"

class Managers(models.Model):

    date = models.DateField(default=date.today)
    title = models.CharField(max_length=300, blank=True, null=True)
    pic1 = models.ImageField(upload_to='static\management_main\img', height_field=None, width_field=None, max_length=100, blank=True, null=True)
    body1 = models.TextField(blank=True)
    pic2 = models.ImageField(upload_to='static\management_main\img', height_field=None, width_field=None, max_length=100, blank=True, null=True, default='static\management_main\img\default.jpg')
    body2 = models.TextField(blank=True)
    pic3 = models.ImageField(upload_to='static\management_main\img', height_field=None, width_field=None, max_length=100, blank=True, null=True, default='static\management_main\img\default.jpg')
    body3 = models.TextField(blank=True)
    pic4 = models.ImageField(upload_to='static\management_main\img', height_field=None, width_field=None, max_length=100, blank=True, null=True, default='static\management_main\img\default.jpg')
    body4 = models.TextField(blank=True)

    def __str__(self):
        return str(self.date)+ ' ' +str(self.title)

    class Meta:
        verbose_name_plural = "Messages from the Managers"
