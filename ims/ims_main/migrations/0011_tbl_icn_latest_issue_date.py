# Generated by Django 3.0.8 on 2020-11-21 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ims_main', '0010_tbl_icn_mhi_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_icn',
            name='latest_issue_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
