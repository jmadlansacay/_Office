# Generated by Django 3.0.8 on 2021-03-09 08:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management_main', '0019_financial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Managers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('pic1', models.ImageField(upload_to='static/media/')),
                ('body1', models.TextField(blank=True)),
                ('pic2', models.ImageField(upload_to='static/media/')),
                ('body2', models.TextField(blank=True)),
                ('pic3', models.ImageField(upload_to='static/media/')),
                ('body3', models.TextField(blank=True)),
                ('pic4', models.ImageField(upload_to='static/media/')),
                ('body4', models.TextField(blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='employees',
            name='employee_status',
            field=models.CharField(blank=True, choices=[('1', 'REGULAR PERMANENT'), ('2', 'PROJECT BASE'), ('3', 'FIXED TERM'), ('4', 'CONSULTANT'), ('5', 'REGULAR AP REP'), ('6', 'PROBATIONARY'), ('7', 'OUTSOURCED')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='employees',
            name='employee_type',
            field=models.CharField(blank=True, choices=[('1', 'EMPLOYEE'), ('2', 'NON-EMPLOYEE'), ('3', 'DIRECT OUTSOURCED'), ('4', 'INDIRECT OUTSOURCED')], max_length=30, null=True),
        ),
    ]
