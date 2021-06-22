from django.db import models
from main_hr.models import hr_master
# Create your models here.

class health_checklist(models.Model):
    CHECK_LIST = [
        ('YES' , 'YES'),
        ('NO', 'NO'),
    ]

    VISIT = [
        ('OFFICIAL' , 'OFFICIAL'),
        ('PERSONAL' , 'PERSONAL'),
    ]
    

    employee = models.ForeignKey(hr_master, to_field='idno', blank=False, null=False, on_delete=models.CASCADE)
    checklist_date = models.DateField(null=False, blank=False)
    nature_of_visit = models.CharField(max_length=10,choices=VISIT, default='OFFICIAL')
    body_temp_check = models.CharField(max_length=3, choices=CHECK_LIST, default='YES')
    sore_throat = models.CharField(max_length=3, choices=CHECK_LIST, default='NO')
    body_pain = models.CharField(max_length=3, choices=CHECK_LIST, default='NO')
    head_ache = models.CharField(max_length=3, choices=CHECK_LIST, default='NO')
    fever = models.CharField(max_length=3, choices=CHECK_LIST, default='NO')
    question_two = models.CharField(max_length=3, choices=CHECK_LIST, default='NO')
    question_three = models.CharField(max_length=3, choices=CHECK_LIST, default='NO')
    question_four = models.CharField(max_length=3, choices=CHECK_LIST, default='NO')
    question_five = models.CharField(max_length=3, choices=CHECK_LIST, default='NO')
    

    def __str__(self):
        return self.employee.idno

    class Meta:
        verbose_name_plural = 'Health Checklist'
