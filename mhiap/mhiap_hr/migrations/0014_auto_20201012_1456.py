# Generated by Django 3.0.8 on 2020-10-12 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mhiap_hr', '0013_auto_20201012_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='hrmaster',
            name='date_employed',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='hrmaster',
            name='date_resigned',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]