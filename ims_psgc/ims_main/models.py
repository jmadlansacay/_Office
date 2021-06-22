from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ref_user_access(models.Model):
    user_access_description = models.CharField(max_length=20, blank=True, null=True)
    sort_order = models.IntegerField(default=0)

    def __str__(self):
        return self.user_access_description

    class Meta:
        verbose_name = "Reference User Access"
        verbose_name_plural = "Reference User Access"


class user_detail(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    user_access = models.ForeignKey(ref_user_access, on_delete=models.DO_NOTHING)
    pic = models.CharField(max_length=20, blank=True, null= True)

    def __str__(self):
        return str(self.username) 

    class Meta:
        verbose_name = "User Detail"
        verbose_name_plural = "User Detail"


class ref_unit(models.Model):
    unit_description = models.CharField(max_length=20, blank=True, null=True, unique=True)

    def __str__(self):
        return self.unit_description

    class Meta:
        verbose_name = "Reference Unit"
        verbose_name_plural = "Reference Unit"


class ref_area(models.Model):
    unit = models.ForeignKey(ref_unit, on_delete=models.CASCADE, to_field='unit_description')
    area = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return str(self.area)

    class Meta:
        verbose_name = "Reference Area"
        verbose_name = "Reference Area"


class ref_mhi_status(models.Model):
    mhi_approve_status_short = models.CharField(max_length=50, blank=False, null=False)
    mhi_approve_status_long = models.CharField(max_length=100, blank=False, null=False)
    model_status = models.CharField(max_length=20, blank=False, null=False)
    mhi_code = models.CharField(max_length=5, blank=False, null = False)
    sort_order = models.IntegerField()

    def __str__(self):
        return self.mhi_code

    class Meta:
        verbose_name = "Reference MHI Status"
        verbose_name_plural = "Reference MHI Status"



class ref_hold(models.Model):
    hold_code = models.CharField(max_length=10, blank=True, null=True)
    hold_description = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.hold_code

    class Meta:
        verbose_name = "Reference Hold"
        verbose_name_plural = "Reference Hold"



# , limit_choices_to={'unit' : "self.unit_id"}

class tbl_icn(models.Model):
    
    ICN_STATUS =[
        ('NEW' , 'NEW'),
        ('REV' , 'REV'),
        ('VOID' , 'VOID'),
    ]
    icn = models.CharField(max_length=5, blank=False, null=False, unique=True)
    unit = models.ForeignKey(ref_unit, on_delete= models.CASCADE)
    area = models.ForeignKey(ref_area, on_delete=models.CASCADE)
    line_id = models.CharField(max_length=20, blank=False, null=False)
    location = models.ForeignKey(user_detail, on_delete=models.SET_NULL, 
        null=True, blank=True, related_name='location', default='')
    designer = models.ForeignKey(user_detail, on_delete=models.SET_NULL, 
        null=True, blank=True, related_name='designer', limit_choices_to={'user_access': 9}, default='')
    pid_checker = models.ForeignKey(user_detail, on_delete=models.SET_NULL, 
        null=True, blank=True, related_name='pid_checker', limit_choices_to={'user_access': 8}, default='')
    spe_checker = models.ForeignKey(user_detail, on_delete=models.SET_NULL, 
        null=True, blank=True, related_name='spe_checker', limit_choices_to={'user_access': 11}, default='')
    checker = models.ForeignKey(user_detail, on_delete=models.SET_NULL, 
        null=True, blank=True, related_name='checker', limit_choices_to={'user_access': 7}, default='')
    pfa_checker = models.ForeignKey(user_detail, on_delete=models.SET_NULL, 
        null=True, blank=True, related_name='pfa_checker', limit_choices_to={'user_access': 10}, default='')
    area_lead = models.ForeignKey(user_detail, on_delete=models.SET_NULL, 
        null=True, blank=True, related_name='area_lead', limit_choices_to={'user_access': 6}, default='')
    mhi_sv = models.ForeignKey(user_detail, on_delete=models.SET_NULL, 
        null=True, blank=True, related_name='mhi_sv', limit_choices_to={'user_access': 5}, default='')
    iso_controller = models.ForeignKey(user_detail, on_delete=models.SET_NULL, 
        null=True, blank=True, related_name='iso_controller', limit_choices_to={'user_access': 4}, default='')
    mhi_status = models.ForeignKey(ref_mhi_status, on_delete=models.SET_NULL, blank=True, null=True)
    latest_issue_date = models.DateField(blank=True, null=True)
    npd = models.FloatField(default=0)
    icn_status = models.CharField(max_length=6, choices=ICN_STATUS, blank=True, null=True, default='NEW')
    

    def __str__(self):
        return str(self.area)+'-'+str(self.line_id)

    class Meta:
        verbose_name = "ICN Table"
        verbose_name_plural = "ICN Table"



class tbl_note1(models.Model):
    icn = models.ForeignKey(tbl_icn, on_delete=models.CASCADE) 
    rev0 = models.DateField(blank=True, null=True)
    rev1 = models.DateField(blank=True, null=True)
    rev2 = models.DateField(blank=True, null=True)
    rev3 = models.DateField(blank=True, null=True)
    rev4 = models.DateField(blank=True, null=True)
    rev5 = models.DateField(blank=True, null=True)
    rev6 = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.icn)

    class Meta:
        verbose_name = "Issue Date"
        verbose_name_plural = "Issue Date"



class tbl_note2(models.Model):
    icn = models.ForeignKey(tbl_icn, on_delete=models.CASCADE)
    hold = models.ForeignKey(ref_hold, on_delete=models.CASCADE)
    item = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return str(self.icn)+'-'+(str(self.hold))

    class Meta:
        verbose_name = "Hold List"
        verbose_name_plural = "Hold List"



class ims_settings(models.Model):
    iso_extract_folder = models.CharField(max_length=300, blank= True, null=True)


    def __str__(self):
        return self.id

    class Meta:
        verbose_name = "IMS Setting"