# Generated by Django 3.0.8 on 2020-09-23 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mhiap_hr', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hr_master',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6),
        ),
    ]
