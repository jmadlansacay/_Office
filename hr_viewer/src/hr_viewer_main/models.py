from django.db import models

# Create your models here.
class TblhrMaster(models.Model):
    employeeid = models.CharField(db_column='EmployeeID', primary_key=True, max_length=4)  # Field name made lowercase.
    employeetype = models.CharField(db_column='EmployeeType', max_length=2)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    middlename = models.CharField(db_column='MiddleName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nickname = models.CharField(db_column='NickName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    employeestatus = models.IntegerField(db_column='EmployeeStatus', blank=True, null=True)  # Field name made lowercase.
    gender = models.IntegerField(db_column='Gender', blank=True, null=True)  # Field name made lowercase.
    civilstatus = models.IntegerField(db_column='CivilStatus', blank=True, null=True)  # Field name made lowercase.
    dateofbirth = models.DateField(db_column='DateofBirth', blank=True, null=True)  # Field name made lowercase.
    birthplace = models.CharField(db_column='Birthplace', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sssno = models.CharField(db_column='SSSNo', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tin = models.CharField(db_column='TIN', max_length=11, blank=True, null=True)  # Field name made lowercase.
    philhealthno = models.CharField(db_column='PhilHealthNo', max_length=14, blank=True, null=True)  # Field name made lowercase.
    pagibigno = models.CharField(db_column='PagIbigNo', max_length=14, blank=True, null=True)  # Field name made lowercase.
    picture = models.CharField(db_column='Picture', max_length=50, blank=True, null=True)  # Field name made lowercase.
    designation = models.CharField(db_column='Designation', max_length=2, blank=True, null=True)  # Field name made lowercase.
    dateemployed = models.DateField(db_column='DateEmployed', blank=True, null=True)  # Field name made lowercase.
    dateresigned = models.DateField(db_column='DateResigned', blank=True, null=True)  # Field name made lowercase.
    shiftcode = models.CharField(db_column='ShiftCode', max_length=2, blank=True, null=True)  # Field name made lowercase.
    projectcode = models.CharField(db_column='ProjectCode', max_length=3, blank=True, null=True)  # Field name made lowercase.
    height = models.FloatField(db_column='Height', blank=True, null=True)  # Field name made lowercase.
    weight = models.FloatField(db_column='Weight', blank=True, null=True)  # Field name made lowercase.
    basic = models.FloatField(db_column='Basic', blank=True, null=True)  # Field name made lowercase.
    effectivitydate = models.DateField(db_column='EffectivityDate', blank=True, null=True)  # Field name made lowercase.
    deminimis = models.FloatField(db_column='Deminimis', blank=True, null=True)  # Field name made lowercase.
    fringe = models.FloatField(db_column='Fringe', blank=True, null=True)  # Field name made lowercase.
    leavecredits = models.FloatField(db_column='LeaveCredits', blank=True, null=True)  # Field name made lowercase.
    slcredits = models.FloatField(db_column='SLCredits', blank=True, null=True)  # Field name made lowercase.
    vlcredits = models.FloatField(db_column='VLCredits', blank=True, null=True)  # Field name made lowercase.
    taxcode = models.CharField(db_column='TaxCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    philhealth = models.FloatField(db_column='PhilHealth', blank=True, null=True)  # Field name made lowercase.
    oldbasic = models.FloatField(db_column='OldBasic', blank=True, null=True)  # Field name made lowercase.
    isict = models.IntegerField(db_column='isICT', blank=True, null=True)  # Field name made lowercase.
    performanceallowance = models.FloatField(db_column='PerformanceAllowance', blank=True, null=True)  # Field name made lowercase.
    positionfee = models.FloatField(db_column='PositionFee', blank=True, null=True)  # Field name made lowercase.
    positionfeename = models.CharField(db_column='PositionFeeName', max_length=2, blank=True, null=True)  # Field name made lowercase.
    performanceallowance0to100 = models.FloatField(db_column='PerformanceAllowance0to100', blank=True, null=True)  # Field name made lowercase.
    singleoccupant = models.FloatField(db_column='SingleOccupant', blank=True, null=True)  # Field name made lowercase.
    relodginghomenetwork = models.FloatField(db_column='RelodgingHomeNetwork', blank=True, null=True)  # Field name made lowercase.
    livingallowance = models.FloatField(db_column='LivingAllowance', blank=True, null=True)  # Field name made lowercase.


    def __str__(self):
        return str(self.lastname)+', '+str(self.firstname)+' '+str(self.nickname)


    class Meta:
        managed = False
        db_table = 'tblHR_Master'
        unique_together = (('employeeid', 'employeetype'),)