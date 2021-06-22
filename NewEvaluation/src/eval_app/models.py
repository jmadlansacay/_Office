from django.db import models
from eval_accounts.models import AccountDetails
# Create your models here.

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

PERIOD = [
        ('Dec. - May', 'Dec. - May'),
        ('May - Nov.', 'May - Nov.')
    ]
class EmployeeEval(models.Model): 
    employee = models.ForeignKey(AccountDetails, blank=True, null=True, on_delete=models.DO_NOTHING, to_field='employee_id')
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
    yr = models.IntegerField(blank=True, null=True)
    period = models.CharField(max_length=20, choices=PERIOD, blank=True, null=True, default='Dec. - May')

    def __str__(self):
        return str(self.employee_id)

    class Meta:
        verbose_name = 'Evaluation'


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

class Evaluation(models.Model):
    
    employee = models.ForeignKey(AccountDetails, on_delete=models.CASCADE, related_name='employee', to_field='employee_id')
    criteria = models.ForeignKey(EvaluationCriteria, on_delete=models.CASCADE)
    self_rating = models.CharField(max_length=3, default='N/A', choices=RATING)
    area_lead = models.ForeignKey(AccountDetails, on_delete=models.SET_NULL, related_name='are_lead', null=True, blank=True, to_field='employee_id')
    area_lead_rating = models.CharField(max_length=3, default='#', choices=RATING)
    project_lead = models.ForeignKey(AccountDetails, on_delete=models.SET_NULL, related_name='project_lead', null=True, blank=True, to_field='employee_id')
    project_lead_rating = models.CharField(max_length=3, default='N/A', choices=RATING)
    manager = models.ForeignKey(AccountDetails, on_delete=models.SET_NULL, related_name='manager', null=True, blank=True, to_field='employee_id')
    manager_rating = models.CharField(max_length=3, default='N/A', choices=RATING)
    actions = models.CharField(max_length=250, blank=True, null=True, default='')
    yr = models.IntegerField(blank=True, null=True)
    period = models.CharField(max_length=20, choices=PERIOD, blank=True, null=True, default='Dec. - May')

    def __str__(self):
        return str(self.employee)+'-'+str(self.criteria)
    
    class Meta:
        verbose_name = 'Skills Evaluation'


class Comments(models.Model):

    RATING = [
        
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
    ]

    INTERNET = [
        ('1','Not at all'),
        ('2','For office use only'),
        ('3','A few times only'),
        ('4','Sometimes'),
        ('5','Often'),
    ]

    TELL_VIOLATION = [
        ('1','Notify to Management'),
        ('2','Notify Project Lead'),
        ('3','Warn him/her'),
        ('4','Just Ignore'),
        ('5','You also do the same'),
    ]

    employee = models.ForeignKey(AccountDetails, on_delete=models.CASCADE, to_field='employee_id')
    yr = models.IntegerField(blank=True, null=True)
    expectation = models.TextField(blank=True, null=True)
    target_position = models.CharField(max_length=50,blank=True, null=True)
    complaints = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=FIN, blank=True, null=True, default='On-Going')
    dispatch_japan = models.CharField(max_length=1, choices=RATING, blank=True, null=True)
    dispatch_singapore = models.CharField(max_length=1, choices=RATING, blank=True, null=True)
    dispatch_philippines = models.CharField(max_length=1, choices=RATING, blank=True, null=True)
    dispatch_us_canada = models.CharField(max_length=1, choices=RATING, blank=True, null=True)
    dispatch_north_europe = models.CharField(max_length=1, choices=RATING, blank=True, null=True)
    dispatch_bangladesh = models.CharField(max_length=1, choices=RATING, blank=True, null=True)
    dispatch_russia = models.CharField(max_length=1, choices=RATING, blank=True, null=True)
    dispatch_africa = models.CharField(max_length=1, choices=RATING, blank=True, null=True)
    fairness_for_all = models.CharField(max_length=1, choices=RATING, blank=True, null=True)
    fairness_for_all_txt = models.TextField(blank=True, null=True)
    terms_of_salary = models.CharField(max_length=1, choices=RATING, blank=True, null=True)
    terms_of_salary_txt = models.TextField(blank=True, null=True)
    rule_on_the_company = models.CharField(max_length=1, choices=RATING, blank=True, null=True)
    rule_on_the_company_txt = models.TextField(blank=True, null=True)
    internet_during_working_hrs = models.CharField(max_length=1, choices=INTERNET, blank=True, null=True, default='1')
    violation_action = models.CharField(max_length=1, choices=TELL_VIOLATION, blank=True, null=True)
    share_knowledge = models.CharField(max_length=1, choices=RATING, blank=True, null=True)
    think_yourself = models.CharField(max_length=1, choices=RATING, blank=True, null=True )


    def __str__(self):
        return str(self.employee) +' '+str(self.yr)

    class Meta:
        verbose_name = 'Comment'
