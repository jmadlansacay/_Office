# Generated by Django 3.0.8 on 2020-11-23 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HReval_eval', '0006_productavilityevaluation_empl_productivity'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeEval',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speed', models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=1, null=True)),
                ('accqlty', models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=1, null=True)),
                ('workeff', models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=1, null=True)),
                ('pdacycle', models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=1, null=True)),
                ('time_panctuality', models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=1, null=True)),
                ('cooperativeness', models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=1, null=True)),
                ('costsaving', models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=1, null=True)),
                ('contribution', models.TextField(blank=True, null=True)),
                ('achievement', models.TextField(blank=True, null=True)),
                ('empl_eval', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='HReval_eval.HrMaster')),
            ],
        ),
        migrations.RemoveField(
            model_name='productavilityevaluation',
            name='empl_productivity',
        ),
        migrations.DeleteModel(
            name='WorkAttitudeEvaluation',
        ),
        migrations.DeleteModel(
            name='ProductavilityEvaluation',
        ),
    ]