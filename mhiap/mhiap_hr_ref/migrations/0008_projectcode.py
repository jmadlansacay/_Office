# Generated by Django 3.0.8 on 2020-09-29 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mhiap_hr_ref', '0007_auto_20200929_1151'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=150)),
                ('project_name', models.CharField(max_length=150)),
                ('project_supervisor', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
    ]