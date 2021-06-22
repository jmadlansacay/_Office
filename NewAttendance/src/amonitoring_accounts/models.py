from django.db import models

# Create your models here.
class UserAccess(models.Model):
    access_description = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.access_description


class user_detail(models.Model):
    mhi_id =  models.CharField(max_length=12, blank=True, null=True, unique=True)
    employee_id = models.CharField(max_length=4, blank=True, null=True, unique=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    first_name =models.CharField(max_length=50, blank=True, null=True)
    nick_name = models.CharField(max_length=50, blank=True, null=True)
    project = models.CharField(max_length=20, blank=True, null=True)
    pic = models.CharField(max_length=50, blank=True, null=True)
    access = models.ForeignKey(UserAccess, on_delete=models.DO_NOTHING, blank=True, null=True, default=5)
    remarks =  models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nick_name

        