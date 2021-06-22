# Generated by Django 2.1.15 on 2021-02-13 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HrgHrRefEmployeestatuscode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeestatusdescription', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'hrg_hr_ref_employeestatuscode',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HrgHrRefGendercode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genderdescription', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'hrg_hr_ref_gendercode',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HrgHrRefProjectcode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectcode', models.CharField(max_length=3)),
                ('projectcodedesc', models.CharField(blank=True, max_length=50, null=True)),
                ('projectname', models.TextField(blank=True, null=True)),
                ('projectsupervisor', models.CharField(blank=True, max_length=50, null=True)),
                ('startdate', models.DateField(blank=True, null=True)),
                ('enddate', models.DateField(blank=True, null=True)),
                ('isactive', models.IntegerField(blank=True, null=True)),
                ('multicharge', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'hrg_hr_ref_projectcode',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HrgHrTblmaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=150, null=True)),
                ('employeeid', models.CharField(max_length=4)),
                ('employeetype', models.CharField(max_length=2)),
                ('lastname', models.CharField(blank=True, max_length=50, null=True)),
                ('firstname', models.CharField(blank=True, max_length=50, null=True)),
                ('middlename', models.CharField(blank=True, max_length=50, null=True)),
                ('nickname', models.CharField(blank=True, max_length=50, null=True)),
                ('civilstatus', models.IntegerField(blank=True, null=True)),
                ('dateofbirth', models.DateField(blank=True, null=True)),
                ('birthplace', models.CharField(blank=True, max_length=50, null=True)),
                ('sssno', models.CharField(blank=True, max_length=12, null=True)),
                ('tin', models.CharField(blank=True, max_length=11, null=True)),
                ('philhealthno', models.CharField(blank=True, max_length=14, null=True)),
                ('pagibigno', models.CharField(blank=True, max_length=14, null=True)),
                ('picture', models.CharField(blank=True, max_length=50, null=True)),
                ('designation', models.CharField(blank=True, max_length=2, null=True)),
                ('dateemployed', models.DateField(blank=True, null=True)),
                ('dateresigned', models.DateField(blank=True, null=True)),
                ('shiftcode', models.CharField(blank=True, max_length=2, null=True)),
                ('height', models.FloatField(blank=True, null=True)),
                ('weight', models.FloatField(blank=True, null=True)),
                ('basic', models.FloatField(blank=True, null=True)),
                ('effectivitydate', models.DateField(blank=True, null=True)),
                ('deminimis', models.FloatField(blank=True, null=True)),
                ('fringe', models.FloatField(blank=True, null=True)),
                ('leavecredits', models.FloatField(blank=True, null=True)),
                ('slcredits', models.FloatField(blank=True, null=True)),
                ('vlcredits', models.FloatField(blank=True, null=True)),
                ('taxcode', models.CharField(blank=True, max_length=50, null=True)),
                ('philhealth', models.FloatField(blank=True, null=True)),
                ('oldbasic', models.FloatField(blank=True, null=True)),
                ('isict', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'hrg_hr_tblmaster',
                'managed': False,
            },
        ),
    ]
