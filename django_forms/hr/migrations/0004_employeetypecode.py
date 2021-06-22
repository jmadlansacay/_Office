# Generated by Django 3.0.8 on 2020-09-30 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0003_employeestatuscode'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeTypeCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeetype', models.CharField(blank=True, max_length=50, null=True)),
                ('prefix', models.CharField(blank=True, max_length=5, null=True)),
            ],
        ),
    ]
