from django.db import models

# Create your models here.

class employee_status_code(models.Model):
    employee_status_description=models.CharField(max_length=50, null=False, blank=False, unique=True)

    def __str__(self):
        return self.employee_status_description

    class Meta:
        verbose_name = 'Employee Status Code'



class project_code(models.Model):
    project_code_description = models.CharField(max_length=25, blank=False, null=False, unique=True)
    project_code_name = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.project_code_description

    class Meta:
        verbose_name = 'Project Code'
