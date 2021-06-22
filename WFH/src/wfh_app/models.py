from django.db import models

# Create your models here.


class wfh_items_category(models.Model):
    category_description = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.category_description

    class Meta:
        verbose_name_plural = 'Item Category'    

