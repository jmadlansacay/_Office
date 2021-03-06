# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Uid(models.Model):
    uid = models.CharField(db_column='UID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FIRSTNAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LASTNAME', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_UID'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class HrgHrIntro(models.Model):
    employeeid = models.CharField(max_length=4, blank=True, null=True)
    msg = models.TextField()

    class Meta:
        managed = False
        db_table = 'hrg_hr_intro'


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


class HrgHrUserDetail(models.Model):
    picture = models.CharField(max_length=50, blank=True, null=True)
    mhiid = models.ForeignKey(AuthUser, models.DO_NOTHING, unique=True)
    pictureurl = models.CharField(max_length=150, blank=True, null=True)
    user_access = models.CharField(max_length=20, blank=True, null=True)
    remarks = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hrg_hr_user_detail'


class HrgTmTransacations(models.Model):
    employeeid = models.CharField(max_length=4, blank=True, null=True)
    employeetype = models.CharField(max_length=2, blank=True, null=True)
    timesheetdate = models.DateField(blank=True, null=True)
    inout = models.IntegerField(blank=True, null=True)
    timepunch = models.TimeField(blank=True, null=True)
    createdby = models.CharField(max_length=50, blank=True, null=True)
    createddate = models.DateTimeField(blank=True, null=True)
    machinename = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hrg_tm_transacations'


class HrgTmTransactionInfo(models.Model):
    employeeid = models.CharField(max_length=4, blank=True, null=True)
    timesheetdate = models.DateField(blank=True, null=True)
    halfday = models.IntegerField(blank=True, null=True)
    reason = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hrg_tm_transaction_info'


class TblhrMaster(models.Model):
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
        db_table = 'tblHR_Master'


class Tblloginnames(models.Model):
    employeeid = models.CharField(db_column='EmployeeID', max_length=4, blank=True, null=True)  # Field name made lowercase.
    loginname = models.CharField(db_column='LogInName', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblLogInNames'


class TblrefCivilstatuscode(models.Model):
    civilstatuscode = models.IntegerField(db_column='CivilStatusCode')  # Field name made lowercase.
    civilstatusdescription = models.CharField(db_column='CivilStatusDescription', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblRef_CivilStatusCode'


class TblrefDesignationcode(models.Model):
    designationcode = models.CharField(db_column='DesignationCode', max_length=3)  # Field name made lowercase.
    designationdescription = models.CharField(db_column='DesignationDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
    designationgroup = models.CharField(db_column='DesignationGroup', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblRef_DesignationCode'


class TblrefEmployeetypecode(models.Model):
    employeetypecode = models.CharField(db_column='EmployeeTypeCode', max_length=2)  # Field name made lowercase.
    employeetypedescription = models.CharField(db_column='EmployeeTypeDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
    employeetypeprefix = models.CharField(db_column='EmployeeTypePrefix', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblRef_EmployeeTypeCode'


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
