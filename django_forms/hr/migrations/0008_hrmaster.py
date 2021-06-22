# Generated by Django 3.0.8 on 2020-09-30 03:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0007_projectcode'),
    ]

    operations = [
        migrations.CreateModel(
            name='HrMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=4, unique=True)),
                ('last_name', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('middle_name', models.CharField(max_length=30)),
                ('civil_status', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hr.CivilStatusCode')),
                ('employee_status', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hr.EmployeeStatusCode')),
                ('employee_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hr.EmployeeTypeCode')),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hr.GenderCode')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hr.ProjectCode')),
            ],
        ),
    ]
