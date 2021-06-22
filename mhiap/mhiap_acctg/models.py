from django.db import models
from mhiap_hr.models import HrMaster

# Create your models here.
class PayrollPeriodReg(models.Model):
    PAY_PERIOD_TYPE =[
        ('REGULAR','REGULAR'),
        ('SPECIAL','SPECIAL')
    ]

    payperiodtype = models.CharField(max_length=7, blank=True, null=True, choices=PAY_PERIOD_TYPE, verbose_name='Pay Period Type')
    paystart = models.DateField(blank=True, null=True, verbose_name='Pay Start')  
    payend = models.DateField(blank=True, null=True, verbose_name='Pay End')  
    modifiedby = models.CharField(max_length=50, blank=True, null=True, verbose_name='Modified By')  
    modifieddate = models.DateField(blank=True, null=True, verbose_name='Modified Date')  
    days = models.FloatField(blank=True, null=True)  
    locked = models.IntegerField(blank=True, null=True)  
    payslipapprove = models.IntegerField(blank=True, null=True)  
    approvedate = models.DateField(blank=True, null=True)  

    def __str__(self):
        return str(self.paystart)+' - '+str(self.payend)+'-'+str(self.payperiodtype)


    class Meta:
        verbose_name = "Standard Payroll Period"
        verbose_name_plural = "Standard Payroll Period"


class StandardRegister(models.Model):
    employeeid = models.ForeignKey(HrMaster, blank=True, null=True,on_delete=models.SET_NULL)  
    paykey = models.ForeignKey(PayrollPeriodReg, blank=True, null=True,on_delete=models.CASCADE)
    basic = models.FloatField(blank=True, null=True)  
    days = models.FloatField(blank=True, null=True)  
    ot150 = models.FloatField(blank=True, null=True)  
    ot200 = models.FloatField(blank=True, null=True)  
    regot150 = models.FloatField(blank=True, null=True)  
    late = models.FloatField(blank=True, null=True)  
    absent = models.FloatField(blank=True, null=True)  
    sl = models.FloatField(blank=True, null=True)  
    vl = models.FloatField(blank=True, null=True)  
    basicold = models.FloatField(blank=True, null=True)  
    daysold = models.FloatField(blank=True, null=True)  
    ot150old = models.FloatField(blank=True, null=True)  
    ot200old = models.FloatField(blank=True, null=True)  
    regot150old = models.FloatField(blank=True, null=True)  
    lateold = models.FloatField(blank=True, null=True)  
    absentold = models.FloatField(blank=True, null=True)  
    slold = models.FloatField(blank=True, null=True)  
    vlold = models.FloatField(blank=True, null=True)  
    halfmonth = models.FloatField(blank=True, null=True)  
    ot150amt = models.FloatField(blank=True, null=True)  
    ot200amt = models.FloatField(blank=True, null=True)  
    regot150amt = models.FloatField(blank=True, null=True)  
    lateamount = models.FloatField(blank=True, null=True)  
    absentamount = models.FloatField(blank=True, null=True)  
    slamount = models.FloatField(blank=True, null=True)  
    vlamount = models.FloatField(blank=True, null=True)  
    halfmonthold = models.FloatField(blank=True, null=True)  
    ot150oldamt = models.FloatField(blank=True, null=True)  
    ot200oldamt = models.FloatField(blank=True, null=True)  
    regot150oldamt = models.FloatField(blank=True, null=True)  
    lateamountold = models.FloatField(blank=True, null=True)  
    absentamountold = models.FloatField(blank=True, null=True)  
    slamountold = models.FloatField(blank=True, null=True)  
    vlamountold = models.FloatField(blank=True, null=True)  
    deminimis = models.FloatField(blank=True, null=True)  
    fringe = models.FloatField(blank=True, null=True)  
    pay13th = models.FloatField(blank=True, null=True)  
    nontaxableadjustment = models.FloatField(blank=True, null=True)  
    taxableadjustment = models.FloatField(blank=True, null=True)  
    vlconversion = models.FloatField(blank=True, null=True)  
    midyear = models.FloatField(blank=True, null=True)  
    allowance = models.FloatField(blank=True, null=True)  
    yearendbonus = models.FloatField(blank=True, null=True)  
    gross = models.FloatField(blank=True, null=True)  
    sss = models.FloatField(blank=True, null=True)  
    philhealth = models.FloatField(blank=True, null=True)  
    pagibig = models.FloatField(blank=True, null=True)  
    nongrosstaxableadjustment = models.FloatField(blank=True, null=True)  
    wtax = models.FloatField(blank=True, null=True)  
    fringetax = models.FloatField(blank=True, null=True)  
    sssloan = models.FloatField(blank=True, null=True)  
    pagibigloan = models.FloatField(blank=True, null=True)  
    companyloan = models.FloatField(blank=True, null=True)  
    nongrossnontaxableadjustment = models.FloatField(blank=True, null=True)  
    taxprovision = models.FloatField(blank=True, null=True)  
    otherdeduction = models.FloatField(blank=True, null=True)  
    netpay = models.FloatField(blank=True, null=True)   
    performanceallowance = models.FloatField(blank=True, null=True)  

    def __str__(self):
        return str(self.employeeid.last_name) +', '+str(self.employeeid.first_name)

    class Meta:
       verbose_name ='Standard Register'
       verbose_name_plural = 'Standard Register'