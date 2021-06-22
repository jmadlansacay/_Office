from django.db import models





class ref_user_access(models.Model):
    user_access_description = models.CharField(max_length=20, blank=True, null=True, unique=True)
    sort_order = models.IntegerField(default=0)

    def __str__(self):
        return self.user_access_description

    class Meta:
        verbose_name = "Reference User Access"
        verbose_name_plural = "Reference User Access"


class user_detail(models.Model):
    username = models.CharField(max_length=50, blank=True, null=True, unique=True)
    user_access = models.ForeignKey(ref_user_access, on_delete=models.DO_NOTHING, to_field='user_access_description')
    pic = models.CharField(max_length=20, blank=True, null= True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    nickname = models.CharField(max_length=50, blank=True, null=True, unique=True)

    def __str__(self):
        return str(self.nickname) 

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
    area = models.CharField(max_length=15, blank=True, null=True, unique=True)

    def __str__(self):
        return str(self.area)

    class Meta:
        verbose_name = "Reference Area"
        verbose_name = "Reference Area"




class ref_mhi_status(models.Model):
    mhi_approve_status_short = models.CharField(max_length=50, blank=False, null=False)
    mhi_approve_status_long = models.CharField(max_length=100, blank=False, null=False)
    model_status = models.CharField(max_length=20, blank=False, null=False)
    mhi_code = models.CharField(max_length=5, blank=False, null = False, unique=True)
    sort_order = models.IntegerField()

    def __str__(self):
        return self.mhi_code

    class Meta:
        verbose_name = "Reference MHI Status"
        verbose_name_plural = "Reference MHI Status"



class tbl_icn(models.Model):
    
    ICN_STATUS =[
        ('NEW' , 'NEW'),
        ('REV' , 'REV'),
        ('VOID' , 'VOID'),
    ]
    icn = models.CharField(max_length=5, blank=False, null=False, unique=True)
    unit = models.ForeignKey(ref_unit, on_delete= models.CASCADE, to_field='unit_description')
    area = models.ForeignKey(ref_area, on_delete=models.CASCADE, to_field='area')
    line_id = models.CharField(max_length=20, blank=False, null=False)
    location = models.ForeignKey(user_detail, on_delete=models.SET_NULL, 
        null=True, blank=True, related_name='location', default='', to_field='nickname')
    designer = models.ForeignKey(user_detail, on_delete=models.SET_NULL, 
        null=True, blank=True, related_name='designer', limit_choices_to={'user_access': '3D Designer'}, default='', to_field='nickname')
    pid_checker = models.ForeignKey(user_detail, on_delete=models.SET_NULL, 
        null=True, blank=True, related_name='pid_checker', limit_choices_to={'user_access': 'PID Checker'}, default='', to_field='nickname')
    spe_checker = models.ForeignKey(user_detail, on_delete=models.SET_NULL, 
        null=True, blank=True, related_name='spe_checker', limit_choices_to={'user_access': 'SPE Checker'}, default='', to_field='nickname')
    checker = models.ForeignKey(user_detail, on_delete=models.SET_NULL, 
        null=True, blank=True, related_name='checker', limit_choices_to={'user_access': 'Checker'}, default='', to_field='nickname')
    pfa_checker = models.ForeignKey(user_detail, on_delete=models.SET_NULL, 
        null=True, blank=True, related_name='pfa_checker', limit_choices_to={'user_access': 'PFA Checker'}, default='', to_field='nickname')
    area_lead = models.ForeignKey(user_detail, on_delete=models.SET_NULL, 
        null=True, blank=True, related_name='area_lead', limit_choices_to={'user_access': 'Area Lead'}, default='', to_field='nickname')
    mhi_sv = models.ForeignKey(user_detail, on_delete=models.SET_NULL, 
        null=True, blank=True, related_name='mhi_sv', limit_choices_to={'user_access': 'MHI SV'}, default='', to_field='nickname')
    iso_controller = models.ForeignKey(user_detail, on_delete=models.SET_NULL, 
        null=True, blank=True, related_name='iso_controller', limit_choices_to={'user_access': 'ISO Controller'}, default='', to_field='nickname')
    mhi_status = models.ForeignKey(ref_mhi_status, on_delete=models.SET_NULL, blank=True, null=True, to_field='mhi_code')
    latest_issue_date = models.DateField(blank=True, null=True)
    npd = models.FloatField(default=0)
    icn_status = models.CharField(max_length=6, choices=ICN_STATUS, blank=True, null=True, default='NEW')


    def __str__(self):
        return str(self.area)+'-'+str(self.line_id)

    class Meta:
        verbose_name = "ICN Table"
        verbose_name_plural = "ICN Table"