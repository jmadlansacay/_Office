from django.db import models

# Create your models here.
class account_details(models.Model):
    mhi_id = models.CharField(max_length=12, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    picture_file = models.CharField(max_length=15, blank=True, null=True)
    access = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.mhi_id

    class Meta:
        verbose_name_plural = 'Accounts'