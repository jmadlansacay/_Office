# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Standard(models.Model):
    employeeid = models.CharField(db_column='EmployeeID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    leave = models.FloatField(db_column='Leave', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_Standard'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)


class Tblaccountno(models.Model):
    employeeid = models.ForeignKey('TblhrMaster', models.DO_NOTHING, db_column='EmployeeID', blank=True, null=True)  # Field name made lowercase.
    employeetype = models.ForeignKey('TblhrMaster', models.DO_NOTHING, db_column='EmployeeType', blank=True, null=True)  # Field name made lowercase.
    accountno = models.CharField(db_column='AccountNo', max_length=10, blank=True, null=True)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=20, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateField(db_column='ModifiedDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAccountNo'


class Tblaccountnobpi(models.Model):
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    accountnumber = models.CharField(db_column='AccountNumber', max_length=10, blank=True, null=True)  # Field name made lowercase.
    employeeid = models.CharField(db_column='EmployeeID', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAccountNoBPI'


class Tblchangeshift(models.Model):
    employeeid = models.CharField(db_column='EmployeeID', max_length=4, blank=True, null=True)  # Field name made lowercase.
    shiftcode = models.CharField(db_column='ShiftCode', max_length=2, blank=True, null=True)  # Field name made lowercase.
    flg = models.IntegerField(db_column='FLG', blank=True, null=True)  # Field name made lowercase.
    dateapplied = models.DateField(db_column='DateApplied', blank=True, null=True)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblChangeShift'


class Tblcomputernames(models.Model):
    employeeid = models.CharField(db_column='EmployeeID', max_length=4, blank=True, null=True)  # Field name made lowercase.
    machinename = models.CharField(db_column='MachineName', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblComputerNames'


class TblcriteriaPersonaltarget(models.Model):
    employeeid = models.CharField(db_column='EmployeeID', max_length=4, blank=True, null=True)  # Field name made lowercase.
    personaltarget = models.TextField(db_column='PersonalTarget', blank=True, null=True)  # Field name made lowercase.
    difficulty = models.CharField(db_column='Difficulty', max_length=10, blank=True, null=True)  # Field name made lowercase.
    targetdue = models.DateField(db_column='TargetDue', blank=True, null=True)  # Field name made lowercase.
    achieved = models.IntegerField(db_column='Achieved', blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateField(db_column='ModifiedDate', blank=True, null=True)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCriteria_PersonalTarget'


class Tbldooraccessid(models.Model):
    employeeid = models.CharField(db_column='EmployeeID', max_length=4, blank=True, null=True)  # Field name made lowercase.
    dooraccessid = models.CharField(db_column='DoorAccessID', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblDoorAccessID'


class Tblextendedotautodtl(models.Model):
    otcode = models.ForeignKey('Tblextendedotautohdr', models.DO_NOTHING, db_column='OTCode', blank=True, null=True)  # Field name made lowercase.
    employeeid = models.ForeignKey('TblhrMaster', models.DO_NOTHING, db_column='EmployeeID', blank=True, null=True)  # Field name made lowercase.
    employeetype = models.ForeignKey('TblhrMaster', models.DO_NOTHING, db_column='EmployeeType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblExtendedOTAutoDTL'


class Tblextendedotautohdr(models.Model):
    otcode = models.CharField(db_column='OTCode', primary_key=True, max_length=4)  # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    maxhrs = models.FloatField(db_column='MaxHrs', blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblExtendedOTAutoHDR'


class Tblforcedleavedtl(models.Model):
    forcedleavedate = models.ForeignKey('Tblforcedleavehdr', models.DO_NOTHING, db_column='ForcedLeaveDate', blank=True, null=True)  # Field name made lowercase.
    employeeid = models.CharField(db_column='EmployeeID', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblForcedLeaveDTL'


class Tblforcedleavehdr(models.Model):
    forcedleavedate = models.DateField(db_column='ForcedLeaveDate', primary_key=True)  # Field name made lowercase.
    forcedleavehours = models.FloatField(db_column='ForcedLeaveHours', blank=True, null=True)  # Field name made lowercase.
    reason = models.TextField(db_column='Reason', blank=True, null=True)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateField(db_column='ModifiedDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblForcedLeaveHDR'


class TblhrAddress(models.Model):
    employeeid = models.CharField(db_column='EmployeeID', max_length=4, blank=True, null=True)  # Field name made lowercase.
    address1 = models.TextField(db_column='Address1', blank=True, null=True)  # Field name made lowercase.
    town1 = models.CharField(db_column='Town1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    province1 = models.CharField(db_column='Province1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address2 = models.TextField(db_column='Address2', blank=True, null=True)  # Field name made lowercase.
    town2 = models.CharField(db_column='Town2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    province2 = models.CharField(db_column='Province2', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblHR_Address'


class TblhrContact(models.Model):
    employeeid = models.ForeignKey('TblhrMaster', models.DO_NOTHING, db_column='EmployeeID', blank=True, null=True)  # Field name made lowercase.
    employeetype = models.ForeignKey('TblhrMaster', models.DO_NOTHING, db_column='EmployeeType', blank=True, null=True)  # Field name made lowercase.
    contactno = models.CharField(db_column='ContactNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    presentaddress = models.TextField(db_column='PresentAddress', blank=True, null=True)  # Field name made lowercase.
    provincialaddress = models.TextField(db_column='ProvincialAddress', blank=True, null=True)  # Field name made lowercase.
    emergencycontact = models.CharField(db_column='EmergencyContact', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bloodtype = models.CharField(db_column='BloodType', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblHR_Contact'


class TblhrLeaveextra(models.Model):
    employeeid = models.ForeignKey('TblhrMaster', models.DO_NOTHING, db_column='EmployeeID', blank=True, null=True)  # Field name made lowercase.
    employeetype = models.ForeignKey('TblhrMaster', models.DO_NOTHING, db_column='EmployeeType', blank=True, null=True)  # Field name made lowercase.
    leavecredits = models.FloatField(db_column='LeaveCredits', blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblHR_LeaveExtra'


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

    class Meta:
        managed = False
        db_table = 'tblHR_Master'
        unique_together = (('employeeid', 'employeetype'),)


class TblhrMasterhist(models.Model):
    employeeid = models.ForeignKey(TblhrMaster, models.DO_NOTHING, db_column='EmployeeID')  # Field name made lowercase.
    employeetype = models.ForeignKey(TblhrMaster, models.DO_NOTHING, db_column='EmployeeType', blank=True, null=True)  # Field name made lowercase.
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
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=20, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblHR_MasterHist'


class TblhrMasterold(models.Model):
    employeeid = models.CharField(db_column='EmployeeID', max_length=4)  # Field name made lowercase.
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

    class Meta:
        managed = False
        db_table = 'tblHR_MasterOld'


class TblhrRfidtime(models.Model):
    employeeid = models.CharField(db_column='EmployeeID', max_length=4, blank=True, null=True)  # Field name made lowercase.
    timesheetdate = models.DateField(db_column='TimeSheetDate', blank=True, null=True)  # Field name made lowercase.
    timepunch = models.TimeField(db_column='TimePunch', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblHR_RFIDTime'


class TblhrSetupUsernames(models.Model):
    username = models.CharField(db_column='UserName', primary_key=True, max_length=50)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=50, blank=True, null=True)  # Field name made lowercase.
    useraccess = models.IntegerField(db_column='UserAccess', blank=True, null=True)  # Field name made lowercase.
    employeeid = models.ForeignKey(TblhrMaster, models.DO_NOTHING, db_column='EmployeeID', blank=True, null=True)  # Field name made lowercase.
    employeetype = models.ForeignKey(TblhrMaster, models.DO_NOTHING, db_column='EmployeeType', blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateField(db_column='ModifiedDate', blank=True, null=True)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblHR_SetUp_UserNames'


class Tblleaveviewer(models.Model):
    employeeid = models.CharField(db_column='EmployeeID', primary_key=True, max_length=4)  # Field name made lowercase.
    isallowed = models.IntegerField(db_column='isAllowed', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblLeaveViewer'


class TblleaveviewerUnder(models.Model):
    employeeid = models.ForeignKey(Tblleaveviewer, models.DO_NOTHING, db_column='EmployeeID', blank=True, null=True)  # Field name made lowercase.
    employeeunder = models.CharField(db_column='EmployeeUnder', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblLeaveViewer_Under'


class Tblloginnames(models.Model):
    employeeid = models.CharField(db_column='EmployeeID', max_length=4, blank=True, null=True)  # Field name made lowercase.
    loginname = models.CharField(db_column='LogInName', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblLogInNames'


class Tblothertaxablebenefits(models.Model):
    employeeid = models.CharField(db_column='EmployeeID', max_length=4, blank=True, null=True)  # Field name made lowercase.
    amt = models.FloatField(db_column='Amt', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50, blank=True, null=True)  # Field name made lowercase.
    yr = models.IntegerField(db_column='YR', blank=True, null=True)  # Field name made lowercase.
    paykey = models.IntegerField(db_column='PayKey', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblOtherTaxableBenefits'


class TblsetupArea(models.Model):
    area = models.CharField(db_column='Area', max_length=50)  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=50, blank=True, null=True)  # Field name made lowercase.
    module = models.CharField(db_column='Module', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSetUp_Area'


class TbltimekeepingExtendedot(models.Model):
    employeeid = models.ForeignKey(TblhrMaster, models.DO_NOTHING, db_column='EmployeeID', blank=True, null=True)  # Field name made lowercase.
    employeetype = models.ForeignKey(TblhrMaster, models.DO_NOTHING, db_column='EmployeeType', blank=True, null=True)  # Field name made lowercase.
    otdate = models.DateField(db_column='OTDate', blank=True, null=True)  # Field name made lowercase.
    hrs = models.FloatField(db_column='Hrs', blank=True, null=True)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblTimeKeeping_ExtendedOT'


class TbltimekeepingLeavedeclined(models.Model):
    employeeid = models.CharField(db_column='EmployeeID', max_length=4, blank=True, null=True)  # Field name made lowercase.
    employeetype = models.CharField(db_column='EmployeeType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    timesheetdate = models.DateField(db_column='TimeSheetDate', blank=True, null=True)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)  # Field name made lowercase.
    approvedby = models.CharField(db_column='ApprovedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    approveddate = models.DateTimeField(db_column='ApprovedDate', blank=True, null=True)  # Field name made lowercase.
    isapproved = models.IntegerField(db_column='isApproved', blank=True, null=True)  # Field name made lowercase.
    reason = models.TextField(db_column='Reason', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    hrs = models.FloatField(db_column='Hrs', blank=True, null=True)  # Field name made lowercase.
    leaveampm = models.IntegerField(db_column='LeaveAMPM', blank=True, null=True)  # Field name made lowercase.
    leavetype = models.CharField(db_column='LeaveType', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblTimeKeeping_LeaveDeclined'


class TbltimekeepingLeavereason(models.Model):
    employeeid = models.ForeignKey(TblhrMaster, models.DO_NOTHING, db_column='EmployeeID', blank=True, null=True)  # Field name made lowercase.
    employeetype = models.ForeignKey(TblhrMaster, models.DO_NOTHING, db_column='EmployeeType', blank=True, null=True)  # Field name made lowercase.
    timesheetdate = models.DateField(db_column='TimeSheetDate', blank=True, null=True)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)  # Field name made lowercase.
    approvedby = models.CharField(db_column='ApprovedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    approveddate = models.DateTimeField(db_column='ApprovedDate', blank=True, null=True)  # Field name made lowercase.
    isapproved = models.IntegerField(db_column='isApproved', blank=True, null=True)  # Field name made lowercase.
    reason = models.TextField(db_column='Reason', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    hrs = models.FloatField(db_column='Hrs', blank=True, null=True)  # Field name made lowercase.
    leaveampm = models.IntegerField(db_column='LeaveAMPM', blank=True, null=True)  # Field name made lowercase.
    leavetype = models.CharField(db_column='LeaveType', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblTimeKeeping_LeaveReason'


class TbltimekeepingLeavereasonProjectexpired(models.Model):
    employeeid = models.CharField(db_column='EmployeeID', max_length=4, blank=True, null=True)  # Field name made lowercase.
    employeetype = models.CharField(db_column='EmployeeType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    timesheetdate = models.DateField(db_column='TimeSheetDate', blank=True, null=True)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)  # Field name made lowercase.
    approvedby = models.CharField(db_column='ApprovedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    approveddate = models.DateTimeField(db_column='ApprovedDate', blank=True, null=True)  # Field name made lowercase.
    isapproved = models.IntegerField(db_column='isApproved', blank=True, null=True)  # Field name made lowercase.
    reason = models.TextField(db_column='Reason', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    hrs = models.FloatField(db_column='Hrs', blank=True, null=True)  # Field name made lowercase.
    leaveampm = models.IntegerField(db_column='LeaveAMPM', blank=True, null=True)  # Field name made lowercase.
    leavetype = models.CharField(db_column='LeaveType', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblTimeKeeping_LeaveReason_ProjectExpired'


class TbltimekeepingTimesheet(models.Model):
    employeeid = models.ForeignKey(TblhrMaster, models.DO_NOTHING, db_column='EmployeeID', blank=True, null=True)  # Field name made lowercase.
    employeetype = models.ForeignKey(TblhrMaster, models.DO_NOTHING, db_column='EmployeeType', blank=True, null=True)  # Field name made lowercase.
    timesheetdate = models.DateField(db_column='TimeSheetDate')  # Field name made lowercase.
    timesheetin = models.TimeField(db_column='TimeSheetIN', blank=True, null=True)  # Field name made lowercase.
    timesheetout = models.TimeField(db_column='TimeSheetOUT', blank=True, null=True)  # Field name made lowercase.
    shiftcode = models.CharField(db_column='ShiftCode', max_length=2, blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    hoursam = models.FloatField(db_column='HoursAM', blank=True, null=True)  # Field name made lowercase.
    leaveam = models.FloatField(db_column='LeaveAM', blank=True, null=True)  # Field name made lowercase.
    hourspm = models.FloatField(db_column='HoursPM', blank=True, null=True)  # Field name made lowercase.
    leavepm = models.FloatField(db_column='LeavePM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblTimeKeeping_TimeSheet'


class TbltimekeepingTimesheethist(models.Model):
    employeeid = models.CharField(db_column='EmployeeID', max_length=4, blank=True, null=True)  # Field name made lowercase.
    employeetype = models.CharField(db_column='EmployeeType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    timesheetdate = models.DateField(db_column='TimeSheetDate')  # Field name made lowercase.
    timesheetin = models.TimeField(db_column='TimeSheetIN', blank=True, null=True)  # Field name made lowercase.
    timesheetout = models.TimeField(db_column='TimeSheetOUT', blank=True, null=True)  # Field name made lowercase.
    shiftcode = models.CharField(db_column='ShiftCode', max_length=2, blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    hoursam = models.FloatField(db_column='HoursAM', blank=True, null=True)  # Field name made lowercase.
    leaveam = models.FloatField(db_column='LeaveAM', blank=True, null=True)  # Field name made lowercase.
    hourspm = models.FloatField(db_column='HoursPM', blank=True, null=True)  # Field name made lowercase.
    leavepm = models.FloatField(db_column='LeavePM', blank=True, null=True)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblTimeKeeping_TimeSheetHist'


class TbltimekeepingTransactions(models.Model):
    employeeid = models.CharField(db_column='EmployeeID', max_length=4, blank=True, null=True)  # Field name made lowercase.
    employeetype = models.CharField(db_column='EmployeeType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    timesheetdate = models.DateField(db_column='TimeSheetDate')  # Field name made lowercase.
    inout = models.IntegerField(db_column='InOut', blank=True, null=True)  # Field name made lowercase.
    timepunch = models.TimeField(db_column='TimePunch', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    machinename = models.CharField(db_column='MachineName', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblTimeKeeping_Transactions'


class TbltimekeepingWfhdates(models.Model):
    employeeid = models.CharField(db_column='EmployeeID', max_length=4, blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblTimeKeeping_WFHDates'


class TblwbsTransactions(models.Model):
    employeeid = models.ForeignKey(TblhrMaster, models.DO_NOTHING, db_column='EmployeeID', blank=True, null=True)  # Field name made lowercase.
    employeetype = models.ForeignKey(TblhrMaster, models.DO_NOTHING, db_column='EmployeeType', blank=True, null=True)  # Field name made lowercase.
    projectcode = models.CharField(db_column='ProjectCode', max_length=3, blank=True, null=True)  # Field name made lowercase.
    area = models.CharField(db_column='Area', max_length=15, blank=True, null=True)  # Field name made lowercase.
    level3 = models.CharField(db_column='Level3', max_length=5, blank=True, null=True)  # Field name made lowercase.
    wbsdate = models.DateField(db_column='WBSDate', blank=True, null=True)  # Field name made lowercase.
    hours = models.FloatField(db_column='Hours', blank=True, null=True)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)  # Field name made lowercase.
    level4 = models.CharField(db_column='Level4', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblWBS_Transactions'


class TblHealthcard(models.Model):
    employeeid = models.ForeignKey(TblhrMaster, models.DO_NOTHING, db_column='EmployeeID', blank=True, null=True)  # Field name made lowercase.
    employeetype = models.ForeignKey(TblhrMaster, models.DO_NOTHING, db_column='EmployeeType', blank=True, null=True)  # Field name made lowercase.
    amount = models.FloatField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.
    paykey = models.IntegerField(db_column='PayKey', blank=True, null=True)  # Field name made lowercase.
    yr = models.IntegerField(db_column='YR', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_HealthCard'


class TblHealthcarddependents(models.Model):
    employeeid = models.CharField(db_column='EmployeeID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    amt = models.IntegerField(db_column='Amt', blank=True, null=True)  # Field name made lowercase.
    paykey = models.IntegerField(db_column='PayKey', blank=True, null=True)  # Field name made lowercase.
    yr = models.IntegerField(db_column='YR', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_HealthCardDependents'
