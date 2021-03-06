# Generated by Django 3.0.8 on 2021-02-26 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainRefEmployeeStatusCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_status_description', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'main_ref_employee_status_code',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MainRefProjectCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_code_description', models.CharField(max_length=25, unique=True)),
                ('project_code_name', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'db_table': 'main_ref_project_code',
                'managed': False,
            },
        ),
    ]
