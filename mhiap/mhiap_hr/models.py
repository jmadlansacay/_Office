from django.db import models
from mhiap_hr_ref.models import EmployeeTypeCode, EmployeeStatusCode, DesignationCode



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
    pic = models.ImageField(upload_to ='hr_pic/', blank=True , null=True)
    date_employed = models.DateField(blank=True, null=True)
    date_resigned = models.DateField(blank=True, null=True)
    height = models.FloatField(default=0, blank=True, null=True)
    weight = models.FloatField(default=0, blank=True, null=True)

    
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



