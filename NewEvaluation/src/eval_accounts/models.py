from django.db import models
from eval_main.models import MainAccountsAccountDetails
# Create your models here.


class UserAccess(models.Model):
    access_description = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.access_description


class AccountDetails(models.Model):

    DEPT =[
        ('ACCOUNTING', 'ACCOUNTING'),
        ('ADMINISTRATION', 'ADMINISTRATION'),
        ('I.T.', 'I.T.'),
        ('OPERATION', 'OPERATION'),
        ('REVIT', 'REVIT'),
        ('',''),
    ]

    mhi_id = models.CharField(max_length=12, blank=True, null=True, unique=True)
    employee_id = models.CharField(max_length=4, blank=True, null=True, unique=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    first_name =models.CharField(max_length=50, blank=True, null=True)
    nick_name = models.CharField(max_length=50, blank=True, null=True)
    project = models.CharField(max_length=20, blank=True, null=True)
    area = models.CharField(max_length=20, blank=True, null=True)
    skill_set = models.CharField(max_length=20, choices=DEPT, null=True, blank=True)
    pic = models.CharField(max_length=12, blank=True, null=True)
    access = models.ForeignKey(UserAccess, on_delete=models.DO_NOTHING, blank=True, null=True, default=5)
    admin = models.IntegerField(default=0)

    def __str__(self):
        return self.nick_name


class EvaluationPeriod(models.Model):

    PERIOD = [
        ('Dec. - May', 'Dec. - May'),
        ('May - Nov.', 'May - Nov.')
    ]
    
    yr = models.IntegerField(blank=True, null=True)
    period = models.CharField(max_length=20, choices=PERIOD, blank=True, null=True, default='Dec. - May')

    def __str__(self):
        return str(self.yr)+' '+str(self.period)

    class Meta:
        verbose_name = 'Evaluation Period'




    



