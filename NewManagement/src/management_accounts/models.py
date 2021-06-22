from django.db import models
from colorfield.fields import ColorField

# Create your models here.
class Projects(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True, unique=True)
    color = ColorField(default='#FF0000')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Projects"
        verbose_name_plural = "Projects"




