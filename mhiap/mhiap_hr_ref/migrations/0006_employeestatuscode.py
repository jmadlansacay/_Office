# Generated by Django 3.0.8 on 2020-09-24 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mhiap_hr_ref', '0005_userdetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeStatusCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=20)),
            ],
        ),
    ]
