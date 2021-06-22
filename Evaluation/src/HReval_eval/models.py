from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ProjectCode(models.Model):
    description = models.CharField(max_length=150, blank=False, null=False)
    project_name = models.CharField(max_length=150, blank=False, null=False)
    project_supervisor = models.CharField(max_length=50, blank=False, null=False)
    start_date = models.DateField(blank=False, null=False)
    end_date = models.DateField(blank=False, null=False)

    def __str__(self):
        return self.description




class EmployeeTypeCode(models.Model):
    description = models.CharField(max_length=50, null=False, blank=True)
    prefix = models.CharField(max_length=4, null=False, blank= True)

    def __str__(self):
        return self.description 


class EmployeeStatusCode(models.Model):
    description = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.description



class DesignationCode(models.Model):
    description = models.CharField(max_length=150, blank=False, null=False)
    designation_group = models.CharField(max_length=150, blank=False, null=False)
    
    def __str__(self):
        return self.description

class HrMaster(models.Model):
    GENDER_CODES =[
        ('Male','Male'),
        ('Female','Female'),
        
    ]
 
    CIVIL_STATUS_CODES =[
        ('Single' , 'Single'),
        ('Married' , 'Married'),
        ('Widowed' , 'Widowed'),
        ('Separated' , 'Separated'),
        ('Annulled' , 'Annulled'),
        ('Confused' , 'Confused'),
    ]

    employee_id = models.CharField(max_length=4, blank=True, null = False, unique = True)
    employee_type = models.ForeignKey(EmployeeTypeCode, on_delete=models.DO_NOTHING, blank=True, null=False)
    employee_status = models.ForeignKey(EmployeeStatusCode, on_delete=models.DO_NOTHING, blank = True, null=False, default=3)
    last_name = models.CharField(max_length=50, blank = True, null = False)
    first_name = models.CharField(max_length=50, blank = True, null = False)
    middle_name = models.CharField(max_length=50, blank = True, null = False)
    nickname = models.CharField(max_length=50, blank = True, null= False)
    gender = models.CharField(max_length=6, choices=GENDER_CODES, blank=True, null=True)
    civil_status = models.CharField(max_length=10, choices=CIVIL_STATUS_CODES, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    birth_place = models.CharField(max_length = 50, null=True, blank= True)
    pic = models.CharField(max_length=20, blank=True , null=True)
    date_employed = models.DateField(blank=True, null=True)
    date_resigned = models.DateField(blank=True, null=True)
    height = models.FloatField(default=0, blank=True, null=True)
    weight = models.FloatField(default=0, blank=True, null=True)
    project_code = models.ForeignKey(ProjectCode, null=True, blank=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.employee_id)+' - '+str(self.last_name)+', '+str(self.first_name)

class HrMasterWorkDetail(models.Model):
    empl = models.OneToOneField(HrMaster, on_delete=models.CASCADE)
    sss_no = models.CharField(max_length=12, blank=True, null=True)
    tin = models.CharField(max_length=11, blank=True, null=True)
    philhealth_no = models.CharField(max_length=14, blank=True, null=True)
    pagibig_no = models.CharField(max_length=14, blank=True, null=True)
    designation = models.ForeignKey(DesignationCode, on_delete=models.DO_NOTHING, blank=True, null=True)


    def __str__(self):
        return self.empl.last_name



class HrMasterAddress(models.Model):
    empl_address = models.OneToOneField(HrMaster, on_delete=models.CASCADE)
    permanent_address = models.TextField()
    permanent_town = models.CharField(max_length=50, blank=True, null=True)
    permanent_province = models.CharField(max_length=50, blank=True, null=True)
    lodging_address = models.TextField()
    lodging_town = models.CharField(max_length=50, blank=True, null=True)
    lodging_province = models.CharField(max_length=50, blank=True, null=True)


    def __str__(self):
        return self.empl_address.last_name



class HrMasterPayrollDetail(models.Model):
    empl_payroll = models.OneToOneField(HrMaster, on_delete=models.CASCADE)
    basic = models.FloatField(blank=True, null=True)
    deminimis = models.FloatField(blank=True, null=True)
    performance_allowance = models.FloatField(blank=True, null=True)
    fringe = models.FloatField(blank=True, null=True)
    leave_credits = models.FloatField(blank=True, null=True)
    sl_credits = models.FloatField(blank=True, null=True)
    vl_credits = models.FloatField(blank=True, null=True)
    account_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.empl_payroll.last_name





class EmployeeEval(models.Model):

    RATING = [
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
    ]

    FIN = [
        ('Submitted', 'Submitted'),
        ('On-Going', 'On-Going')
    ]

    empl_eval = models.OneToOneField(HrMaster, on_delete=models.CASCADE)
    speed = models.CharField(max_length=1, choices=RATING, blank=True, null=True, default='0')
    accqlty = models.CharField(max_length=1, choices=RATING, blank=True, null=True, default='0')
    workeff = models.CharField(max_length=1, choices=RATING, blank=True, null=True, default='0')
    pdacycle = models.CharField(max_length=1, choices=RATING, blank=True, null=True, default='0')
    time_panctuality = models.CharField(max_length=1, choices=RATING, blank=True, null=True, default='0')
    cooperativeness =  models.CharField(max_length=1, choices=RATING, blank=True, null=True, default='0')
    harmony =  models.CharField(max_length=1, choices=RATING, blank=True, null=True, default='0')
    costsaving = models.CharField(max_length=1, choices=RATING, blank=True, null=True, default='0')
    contribution = models.TextField(blank=True, null=True)
    loyalty= models.CharField(max_length=1, choices=RATING, blank=True, null=True, default='0')
    team_player= models.CharField(max_length=1, choices=RATING, blank=True, null=True, default='0')
    achievement = models.TextField(blank=True, null=True)
    user_submit = models.CharField(max_length=20, choices=FIN, blank=True, null=True, default='On-Going')
    lead_submit = models.CharField(max_length=20, choices=FIN, blank=True, null=True, default='On-Going')


    def __str__(self):
        return str(self.empl_eval.last_name)
 


class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    permission = models.CharField(max_length=100, default='0')
    project_code = models.ForeignKey(ProjectCode, null=True, blank=True, on_delete=models.SET_NULL)
    employee = models.ForeignKey(HrMaster ,blank=True, null=True, on_delete=models.SET_NULL)


    def __str__(self):
        return str(self.user)+'-'+str(self.user.last_name)