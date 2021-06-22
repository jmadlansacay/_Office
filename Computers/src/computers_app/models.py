from django.db import models

# Create your models here.

class ItemType(models.Model):
    item_description = models.CharField(max_length=50, blank=False, null=False, unique=True)

    def __str__(self):
        return self.item_description

    class Meta:
        verbose_name_plural = 'Item Types'



class ComputerModel(models.Model):
    model_description = models.CharField(max_length=50, blank=False, null=False, unique=True)
    item_type = models.ForeignKey(ItemType, blank=True, null=True, on_delete=models.SET_NULL, to_field='item_description')
    
    def __str__(self):
        return self.model_description

    class Meta:
        verbose_name_plural = 'Computer Models'    



class UserNames(models.Model):
    idno = models.CharField(unique=True, max_length=4)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null= True)
    nick_name = models.CharField(max_length=50, blank=True, null=True, unique=True)

    def __str__(self):
        return self.nick_name

    class Meta:
        verbose_name_plural = "Users"


class computer_inventory(models.Model):

    STAT = [
        ('IN-USE','IN-USE'),
        ('IN-STOCK','IN-STOCK'),
        ('DEFECTIVE', 'DEFECTIVE')
    ]

    item_code = models.CharField(max_length=15, blank=True, null= True)
    item_model = models.ForeignKey(ComputerModel, blank=True, null=True, on_delete=models.SET_NULL, to_field='model_description')
    device_name = models.CharField(max_length=50, blank=True, null=True)
    serial_number = models.CharField(max_length=50, blank=True, null=True)
    item_status = models.CharField(max_length=50, blank=True, null=True, choices=STAT, default='IN-STOCK')
    item_user = models.ForeignKey(UserNames, blank=True, null=True, on_delete=models.SET_NULL, to_field='nick_name')


    def __str__(self):
        return self.item_code


    class Meta:
        verbose_name_plural = 'Inventory'
    