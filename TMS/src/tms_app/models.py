from django.db import models

# Create your models here.
class tms_main(models.Model):
    uname = models.CharField(max_length=150)