# Generated by Django 3.0.8 on 2020-11-17 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ims_main', '0004_ref_area_ref_unit'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_icn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icn', models.CharField(max_length=5, unique=True)),
                ('area', models.ForeignKey(limit_choices_to={'unit': models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ims_main.ref_unit')}, on_delete=django.db.models.deletion.CASCADE, to='ims_main.ref_area')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ims_main.ref_unit')),
            ],
        ),
    ]
