# Generated by Django 3.0.8 on 2020-09-23 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mhiap_hr_ref', '0002_civil_status_code_employee_status_code'),
    ]

    operations = [
        migrations.DeleteModel(
            name='civil_status_code',
        ),
        migrations.DeleteModel(
            name='employee_status_code',
        ),
        migrations.DeleteModel(
            name='gender_code',
        ),
    ]