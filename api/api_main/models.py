from django.db import models

# Create your models here.
class ref_user_access(models.Model):
    user_access_description = models.CharField(max_length=20, blank=True, null=True)
    sort_order = models.IntegerField(default=0)

    def __str__(self):
        return self.user_access_description

    class Meta:
        verbose_name = "Reference User Access"
        verbose_name_plural = "Reference User Access"