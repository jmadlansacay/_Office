# Generated by Django 3.0.8 on 2020-11-21 00:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HReval_eval', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HrMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(blank=True, max_length=4, unique=True)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('first_name', models.CharField(blank=True, max_length=50)),
                ('middle_name', models.CharField(blank=True, max_length=50)),
                ('nickname', models.CharField(blank=True, max_length=50)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6, null=True)),
                ('civil_status', models.CharField(blank=True, choices=[('Single', 'Single'), ('Married', 'Married'), ('Widowed', 'Widowed'), ('Separated', 'Separated'), ('Annulled', 'Annulled'), ('Confused', 'Confused')], max_length=10, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('birth_place', models.CharField(blank=True, max_length=50, null=True)),
                ('pic', models.ImageField(blank=True, null=True, upload_to='hr_pic/')),
                ('date_employed', models.DateField(blank=True, null=True)),
                ('date_resigned', models.DateField(blank=True, null=True)),
                ('height', models.FloatField(blank=True, default=0, null=True)),
                ('weight', models.FloatField(blank=True, default=0, null=True)),
                ('employee_status', models.ForeignKey(blank=True, default=3, on_delete=django.db.models.deletion.DO_NOTHING, to='HReval_eval.EmployeeStatusCode')),
                ('employee_type', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='HReval_eval.EmployeeTypeCode')),
            ],
        ),
        migrations.CreateModel(
            name='HrMasterWorkDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sss_no', models.CharField(blank=True, max_length=12, null=True)),
                ('tin', models.CharField(blank=True, max_length=11, null=True)),
                ('philhealth_no', models.CharField(blank=True, max_length=14, null=True)),
                ('pagibig_no', models.CharField(blank=True, max_length=14, null=True)),
                ('designation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='HReval_eval.DesignationCode')),
                ('empl', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='HReval_eval.HrMaster')),
            ],
        ),
        migrations.CreateModel(
            name='HrMasterPayrollDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basic', models.FloatField(blank=True, null=True)),
                ('deminimis', models.FloatField(blank=True, null=True)),
                ('performance_allowance', models.FloatField(blank=True, null=True)),
                ('fringe', models.FloatField(blank=True, null=True)),
                ('leave_credits', models.FloatField(blank=True, null=True)),
                ('sl_credits', models.FloatField(blank=True, null=True)),
                ('vl_credits', models.FloatField(blank=True, null=True)),
                ('account_number', models.CharField(blank=True, max_length=20, null=True)),
                ('empl_payroll', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='HReval_eval.HrMaster')),
            ],
        ),
        migrations.CreateModel(
            name='HrMasterAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permanent_address', models.TextField()),
                ('permanent_town', models.CharField(blank=True, max_length=50, null=True)),
                ('permanent_province', models.CharField(blank=True, max_length=50, null=True)),
                ('lodging_address', models.TextField()),
                ('lodging_town', models.CharField(blank=True, max_length=50, null=True)),
                ('lodging_province', models.CharField(blank=True, max_length=50, null=True)),
                ('empl_address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='HReval_eval.HrMaster')),
            ],
        ),
    ]
