# Generated by Django 3.0.8 on 2021-03-22 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eval_app', '0009_auto_20210317_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='status',
            field=models.CharField(blank=True, choices=[('Submitted', 'Submitted'), ('On-Going', 'On-Going')], default='On-Going', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='area_lead_rating',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='#', max_length=3),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='manager_rating',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='N/A', max_length=3),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='project_lead_rating',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='N/A', max_length=3),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='self_rating',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='N/A', max_length=3),
        ),
    ]