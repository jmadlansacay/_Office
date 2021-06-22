# Generated by Django 3.0.8 on 2020-11-17 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ims_main', '0006_auto_20201117_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_icn',
            name='checker',
            field=models.ForeignKey(blank=True, default='', limit_choices_to={'user_access': 7}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='checker', to='ims_main.user_detail'),
        ),
        migrations.AddField(
            model_name='tbl_icn',
            name='pid_checker',
            field=models.ForeignKey(blank=True, default='', limit_choices_to={'user_access': 8}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pid_checker', to='ims_main.user_detail'),
        ),
        migrations.AddField(
            model_name='tbl_icn',
            name='spe_checker',
            field=models.ForeignKey(blank=True, default='', limit_choices_to={'user_access': 11}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='spe_checker', to='ims_main.user_detail'),
        ),
        migrations.AlterField(
            model_name='tbl_icn',
            name='designer',
            field=models.ForeignKey(blank=True, default='', limit_choices_to={'user_access': 9}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='designer', to='ims_main.user_detail'),
        ),
        migrations.AlterField(
            model_name='tbl_icn',
            name='location',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='location', to='ims_main.user_detail'),
        ),
    ]
