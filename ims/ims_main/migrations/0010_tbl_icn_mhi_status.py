# Generated by Django 3.0.8 on 2020-11-18 00:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ims_main', '0009_ref_mhi_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_icn',
            name='mhi_status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ims_main.ref_mhi_status'),
        ),
    ]
