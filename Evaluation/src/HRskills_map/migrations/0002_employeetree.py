# Generated by Django 3.0.8 on 2020-12-03 03:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HReval_eval', '0015_auto_20201130_1341'),
        ('HRskills_map', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeTree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_set', models.CharField(blank=True, choices=[('ACCOUNTING', 'ACCOUNTING'), ('ADMINISTRATION', 'ADMINISTRATION'), ('IT', 'IT'), ('OPERATION', 'OPERATION')], max_length=20, null=True)),
                ('access', models.IntegerField(default=1)),
                ('project_area', models.CharField(blank=True, max_length=20, null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HReval_eval.HrMaster')),
            ],
        ),
    ]
