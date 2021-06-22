from django.db import models
from HReval_eval.models import HrMaster

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    series = models.IntegerField()

    def __str__(self):
        return str(self.name)


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=3, blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.name)+' - '+str(self.description)


class EvaluationCriteria(models.Model):
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    description = models.CharField(max_length=150, blank=True, null=True)
    group = models.CharField(max_length=250, blank=True, null=True)    

    def __str__(self):
        return str(self.description)


class EmployeeTree(models.Model):
    
    DEPT =[
        ('ACCOUNTING', 'ACCOUNTING'),
        ('ADMINISTRATION', 'ADMINISTRATION'),
        ('I.T.', 'I.T.'),
        ('OPERATION', 'OPERATION'),
        ('REVIT', 'REVIT'),
    ]

    employee = models.ForeignKey(HrMaster, on_delete=models.CASCADE)
    skill_set = models.CharField(max_length=20, choices=DEPT, null=True, blank=True)
    access = models.IntegerField(default=1)
    project_area = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return str(self.employee)



class Evaluation(models.Model):
    RATING = [
        ('#' , '#'),
        ('0' , '0'),
        ('1' , '1'),
        ('2' , '2'),
        ('3' , '3'),
        ('4' , '4'),
    ]

    employee = models.ForeignKey(HrMaster, on_delete=models.CASCADE, related_name='employee')
    criteria = models.ForeignKey(EvaluationCriteria, on_delete=models.CASCADE)
    self_rating = models.CharField(max_length=3, default='N/A', choices=RATING)
    area_lead = models.ForeignKey(HrMaster, on_delete=models.SET_NULL, related_name='are_lead', null=True, blank=True)
    area_lead_rating = models.CharField(max_length=3, default='#', choices=RATING)
    project_lead = models.ForeignKey(HrMaster, on_delete=models.SET_NULL, related_name='project_lead', null=True, blank=True)
    project_lead_rating = models.CharField(max_length=3, default='N/A', choices=RATING)
    manager = models.ForeignKey(HrMaster, on_delete=models.SET_NULL, related_name='manager', null=True, blank=True)
    manager_rating = models.CharField(max_length=3, default='N/A', choices=RATING)
    actions = models.CharField(max_length=250, blank=True, null=True, default='')

    def __str__(self):
        return str(self.employee)+'-'+str(self.criteria)


class comandsugg(models.Model):
    employee = models.ForeignKey(HrMaster, on_delete=models.CASCADE)
    expectations = models.TextField(blank=True, null=True, default='')
    target_position = models.CharField(max_length=50, blank=True, null =True)
    complaints = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.employee)

    class Meta:
        verbose_name = 'Comments and Suggetion'



