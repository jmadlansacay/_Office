# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Vwstandardregister(models.Model):
    employeetypeprefix = models.CharField(db_column='EmployeeTypePrefix', max_length=4, blank=True, null=True)  # Field name made lowercase.
    employeeid = models.CharField(db_column='EmployeeID', max_length=4, blank=True, null=True)  # Field name made lowercase.
    paykey = models.IntegerField(db_column='PayKey', blank=True, null=True)  # Field name made lowercase.
    namer = models.CharField(db_column='Namer', max_length=158, blank=True, null=True)  # Field name made lowercase.
    basic = models.FloatField(db_column='Basic', blank=True, null=True)  # Field name made lowercase.
    days = models.FloatField(db_column='Days', blank=True, null=True)  # Field name made lowercase.
    ot150 = models.FloatField(db_column='OT150', blank=True, null=True)  # Field name made lowercase.
    ot200 = models.FloatField(db_column='OT200', blank=True, null=True)  # Field name made lowercase.
    regot150 = models.FloatField(db_column='REGOT150', blank=True, null=True)  # Field name made lowercase.
    late = models.FloatField(db_column='Late', blank=True, null=True)  # Field name made lowercase.
    absent = models.FloatField(db_column='Absent', blank=True, null=True)  # Field name made lowercase.
    sl = models.FloatField(db_column='SL', blank=True, null=True)  # Field name made lowercase.
    vl = models.FloatField(db_column='VL', blank=True, null=True)  # Field name made lowercase.
    basicold = models.FloatField(db_column='BasicOld', blank=True, null=True)  # Field name made lowercase.
    daysold = models.FloatField(db_column='DaysOld', blank=True, null=True)  # Field name made lowercase.
    ot150old = models.FloatField(db_column='OT150Old', blank=True, null=True)  # Field name made lowercase.
    ot200old = models.FloatField(db_column='OT200Old', blank=True, null=True)  # Field name made lowercase.
    regot150old = models.FloatField(db_column='REGOT150Old', blank=True, null=True)  # Field name made lowercase.
    lateold = models.FloatField(db_column='LateOld', blank=True, null=True)  # Field name made lowercase.
    absentold = models.FloatField(db_column='AbsentOld', blank=True, null=True)  # Field name made lowercase.
    slold = models.FloatField(db_column='SLOld', blank=True, null=True)  # Field name made lowercase.
    vlold = models.FloatField(db_column='VLOld', blank=True, null=True)  # Field name made lowercase.
    halfmonth = models.FloatField(db_column='HalfMonth', blank=True, null=True)  # Field name made lowercase.
    ot150amt = models.FloatField(db_column='OT150Amt', blank=True, null=True)  # Field name made lowercase.
    ot200amt = models.FloatField(db_column='OT200Amt', blank=True, null=True)  # Field name made lowercase.
    regot150amt = models.FloatField(db_column='REGOT150Amt', blank=True, null=True)  # Field name made lowercase.
    lateamount = models.FloatField(db_column='LateAmount', blank=True, null=True)  # Field name made lowercase.
    absentamount = models.FloatField(db_column='AbsentAmount', blank=True, null=True)  # Field name made lowercase.
    slamount = models.FloatField(db_column='SLAmount', blank=True, null=True)  # Field name made lowercase.
    vlamount = models.FloatField(db_column='VLAmount', blank=True, null=True)  # Field name made lowercase.
    halfmonthold = models.FloatField(db_column='HalfMonthOld', blank=True, null=True)  # Field name made lowercase.
    ot150oldamt = models.FloatField(db_column='OT150OldAmt', blank=True, null=True)  # Field name made lowercase.
    ot200oldamt = models.FloatField(db_column='OT200OldAmt', blank=True, null=True)  # Field name made lowercase.
    regot150oldamt = models.FloatField(db_column='REGOT150OldAmt', blank=True, null=True)  # Field name made lowercase.
    lateamountold = models.FloatField(db_column='LateAmountOld', blank=True, null=True)  # Field name made lowercase.
    absentamountold = models.FloatField(db_column='AbsentAmountOld', blank=True, null=True)  # Field name made lowercase.
    slamountold = models.FloatField(db_column='SLAmountOld', blank=True, null=True)  # Field name made lowercase.
    vlamountold = models.FloatField(db_column='VLAmountOld', blank=True, null=True)  # Field name made lowercase.
    deminimis = models.FloatField(db_column='Deminimis', blank=True, null=True)  # Field name made lowercase.
    fringe = models.FloatField(db_column='Fringe', blank=True, null=True)  # Field name made lowercase.
    pay13th = models.FloatField(db_column='Pay13th', blank=True, null=True)  # Field name made lowercase.
    nontaxableadjustment = models.FloatField(db_column='NonTaxableAdjustment', blank=True, null=True)  # Field name made lowercase.
    taxableadjustment = models.FloatField(db_column='TaxableAdjustment', blank=True, null=True)  # Field name made lowercase.
    vlconversion = models.FloatField(db_column='VLConversion', blank=True, null=True)  # Field name made lowercase.
    midyear = models.FloatField(db_column='MidYear', blank=True, null=True)  # Field name made lowercase.
    allowance = models.FloatField(db_column='Allowance', blank=True, null=True)  # Field name made lowercase.
    yearendbonus = models.FloatField(db_column='YearEndBonus', blank=True, null=True)  # Field name made lowercase.
    gross = models.FloatField(db_column='Gross', blank=True, null=True)  # Field name made lowercase.
    sss = models.FloatField(db_column='SSS', blank=True, null=True)  # Field name made lowercase.
    philhealth = models.FloatField(db_column='PhilHealth', blank=True, null=True)  # Field name made lowercase.
    pagibig = models.FloatField(db_column='PagIbig', blank=True, null=True)  # Field name made lowercase.
    nongrosstaxableadjustment = models.FloatField(db_column='NonGrossTaxableAdjustment', blank=True, null=True)  # Field name made lowercase.
    wtax = models.FloatField(db_column='WTAX', blank=True, null=True)  # Field name made lowercase.
    fringetax = models.FloatField(db_column='FringeTax', blank=True, null=True)  # Field name made lowercase.
    sssloan = models.FloatField(db_column='SSSLoan', blank=True, null=True)  # Field name made lowercase.
    pagibigloan = models.FloatField(db_column='PagIbigLoan', blank=True, null=True)  # Field name made lowercase.
    companyloan = models.FloatField(db_column='CompanyLoan', blank=True, null=True)  # Field name made lowercase.
    nongrossnontaxableadjustment = models.FloatField(db_column='NonGrossNonTaxableAdjustment', blank=True, null=True)  # Field name made lowercase.
    taxprovision = models.FloatField(db_column='TaxProvision', blank=True, null=True)  # Field name made lowercase.
    otherdeduction = models.FloatField(db_column='OtherDeduction', blank=True, null=True)  # Field name made lowercase.
    netpay = models.FloatField(db_column='NetPay', blank=True, null=True)  # Field name made lowercase.
    designationdescription = models.CharField(db_column='DesignationDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
    performanceallowance = models.FloatField(db_column='PerformanceAllowance', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vwStandardRegister'
