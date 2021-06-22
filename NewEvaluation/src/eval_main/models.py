from django.db import models

# Create your models here.
class MainRefEmployeeStatusCode(models.Model):
    employee_status_description = models.CharField(unique=True, max_length=50)

    def __str__(self):
        return self.employee_status_description

    class Meta:
        managed = False
        db_table = 'main_ref_employee_status_code'


class MainRefProjectCode(models.Model):
    project_code_description = models.CharField(unique=True, max_length=25)
    project_code_name = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
            return self.project_code_description

    class Meta:
        managed = False
        db_table = 'main_ref_project_code'


class MainHrHrMaster(models.Model):
    idno = models.CharField(unique=True, max_length=4)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    nick_name = models.CharField(unique=True, max_length=50, blank=True, null=True)
    mhi_id = models.CharField(max_length=12, blank=True, null=True)
    gender = models.CharField(max_length=6, blank=True, null=True)
    picture = models.CharField(max_length=15, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    employee_status = models.ForeignKey('MainRefEmployeeStatusCode', models.DO_NOTHING , to_field='employee_status_description')
    project = models.ForeignKey('MainRefProjectCode', models.DO_NOTHING, to_field='project_code_description')

    def __str__(self):
        return self.last_name

    class Meta:
        managed = False
        db_table = 'main_hr_hr_master'


class MainAccountsAccountDetails(models.Model):
    mhi_id = models.CharField(max_length=12, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    picture_file = models.CharField(max_length=15, blank=True, null=True)
    access = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return str(self.mhi_id)+' '+str(self.last_name)+', '+str(self.first_name)

    class Meta:
        managed = False
        db_table = 'main_accounts_account_details'