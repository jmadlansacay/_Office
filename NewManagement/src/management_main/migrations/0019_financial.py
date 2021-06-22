# Generated by Django 3.0.8 on 2021-03-02 04:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management_main', '0018_auto_20210301_1320'),
    ]

    operations = [
        migrations.CreateModel(
            name='Financial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('pic', models.ImageField(upload_to='static/media/')),
            ],
        ),
    ]
