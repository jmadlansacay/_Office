# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TblrefProjectcode(models.Model):
    projectcode = models.CharField(db_column='ProjectCode', max_length=3)  # Field name made lowercase.
    projectcodedesc = models.CharField(db_column='ProjectCodeDesc', max_length=50, blank=True, null=True)  # Field name made lowercase.
    projectname = models.TextField(db_column='ProjectName', blank=True, null=True)  # Field name made lowercase.
    projectsupervisor = models.CharField(db_column='ProjectSupervisor', max_length=50, blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    isactive = models.IntegerField(db_column='isActive', blank=True, null=True)  # Field name made lowercase.
    multicharge = models.IntegerField(db_column='MultiCharge', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblRef_ProjectCode'
