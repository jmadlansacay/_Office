# Generated by Django 3.0.8 on 2021-05-20 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainAccountsAccountDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mhi_id', models.CharField(blank=True, max_length=12, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('picture_file', models.CharField(blank=True, max_length=15, null=True)),
                ('access', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'db_table': 'main_accounts_account_details',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MainHrHrMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idno', models.CharField(max_length=4, unique=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=50, null=True)),
                ('nick_name', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('mhi_id', models.CharField(blank=True, max_length=12, null=True)),
                ('gender', models.CharField(blank=True, max_length=6, null=True)),
                ('picture', models.CharField(blank=True, max_length=15, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'main_hr_hr_master',
                'managed': False,
            },
        ),
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
