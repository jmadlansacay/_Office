# Generated by Django 3.0.8 on 2020-10-09 02:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mhiap_hr', '0008_hrmaster_employee_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='HrMasterWorkDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sss_no', models.CharField(blank=True, max_length=12, null=True)),
                ('tin', models.CharField(blank=True, max_length=11, null=True)),
                ('philhealth_no', models.CharField(blank=True, max_length=14, null=True)),
                ('pagibig_no', models.CharField(blank=True, max_length=12, null=True)),
                ('employee_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mhiap_hr.HrMaster')),
            ],
        ),
    ]
