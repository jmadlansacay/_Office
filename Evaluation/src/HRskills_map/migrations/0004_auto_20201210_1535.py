# Generated by Django 3.0.8 on 2020-12-10 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HReval_eval', '0016_employeeeval_harmony'),
        ('HRskills_map', '0003_auto_20201203_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeetree',
            name='skill_set',
            field=models.CharField(blank=True, choices=[('ACCOUNTING', 'ACCOUNTING'), ('ADMINISTRATION', 'ADMINISTRATION'), ('I.T.', 'I.T.'), ('OPERATION', 'OPERATION'), ('REVIT', 'REVIT')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='area_lead_rating',
            field=models.CharField(choices=[('#', '#'), ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='#', max_length=3),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee', to='HReval_eval.HrMaster'),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='manager_rating',
            field=models.CharField(choices=[('#', '#'), ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='N/A', max_length=3),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='project_lead_rating',
            field=models.CharField(choices=[('#', '#'), ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='N/A', max_length=3),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='self_rating',
            field=models.CharField(choices=[('#', '#'), ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='N/A', max_length=3),
        ),
    ]
