# Generated by Django 3.0.8 on 2021-02-05 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ims_main', '0006_auto_20210205_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_icn',
            name='location',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='location', to='ims_main.user_detail', to_field='nickname'),
        ),
    ]
