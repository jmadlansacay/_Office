# Generated by Django 3.0.8 on 2020-09-23 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mhiap_hr_ref', '0004_employeetypecode'),
        ('mhiap_hr', '0004_auto_20200923_1716'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='hr_master',
            new_name='HrMaster',
        ),
    ]