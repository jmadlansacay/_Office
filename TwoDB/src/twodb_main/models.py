from django.db import models

# Create your models here.


class HrgHrRefEmployeestatuscode(models.Model):
    employeestatusdescription = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'hrg_hr_ref_employeestatuscode'


class HrgHrRefGendercode(models.Model):
    genderdescription = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'hrg_hr_ref_gendercode'


class HrgHrRefProjectcode(models.Model):
    projectcode = models.CharField(max_length=3)
    projectcodedesc = models.CharField(max_length=50, blank=True, null=True)
    projectname = models.TextField(blank=True, null=True)
    projectsupervisor = models.CharField(max_length=50, blank=True, null=True)
    startdate = models.DateField(blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)
    isactive = models.IntegerField(blank=True, null=True)
    multicharge = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hrg_hr_ref_projectcode'





class HrgHrTblmaster(models.Model):
    username = models.CharField(max_length=150, blank=True, null=True)
    employeeid = models.CharField(max_length=4)
    employeetype = models.CharField(max_length=2)
    lastname = models.CharField(max_length=50, blank=True, null=True)
    firstname = models.CharField(max_length=50, blank=True, null=True)
    middlename = models.CharField(max_length=50, blank=True, null=True)
    nickname = models.CharField(max_length=50, blank=True, null=True)
    employeestatus = models.ForeignKey(HrgHrRefEmployeestatuscode, models.DO_NOTHING, blank=True, null=True)
    gender = models.ForeignKey(HrgHrRefGendercode, models.DO_NOTHING, blank=True, null=True)
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
    projectcode = models.ForeignKey(HrgHrRefProjectcode, models.DO_NOTHING, blank=True, null=True)
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

    class Meta:
        managed = False
        db_table = 'hrg_hr_tblmaster'