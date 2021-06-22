from django.db import models

# Create your models here.
class mhi_user(models.Model):
    employee_number = models.CharField(max_length=4, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    nick_name = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.nick_name

    class Meta:
        verbose_name_plural = 'Users'