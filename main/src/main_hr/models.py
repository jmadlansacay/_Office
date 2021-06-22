from django.db import models
from main_ref.models import employee_status_code, project_code
# Create your models here.


class hr_master(models.Model):
    GENDER_CODE =[
        ('MALE','MALE'),
        ('FEMALE', 'FEMALE')
    ]
    idno = models.CharField(max_length=4,blank=False,null=False, unique=True)
    employee_status = models.ForeignKey(employee_status_code, to_field='employee_status_description', on_delete=models.DO_NOTHING)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    nick_name = models.CharField(max_length=50, blank=True, null=True, unique=True)
    mhi_id = models.CharField(max_length=12, blank=True, null=True)
    gender = models.CharField(max_length=6, choices=GENDER_CODE, blank=True, null=True, default='MALE')
    project = models.ForeignKey(project_code, to_field='project_code_description', on_delete=models.DO_NOTHING)
    picture = models.CharField(max_length=15, null=True, blank=True)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.idno

    class META:
        verbose_name_plural = 'HR Master'
    
