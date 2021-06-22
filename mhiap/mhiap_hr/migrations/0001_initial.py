# Generated by Django 3.0.8 on 2020-09-23 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hr_master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=4)),
                ('gender', models.CharField(choices=[('Male', 'Female')], max_length=5)),
            ],
        ),
    ]
