# Generated by Django 3.0.8 on 2021-03-19 02:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management_main', '0027_auto_20210318_0809'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeadCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('source_file', models.ImageField(blank=True, default='static\\management_main\\img\\default.jpg', null=True, upload_to='static\\management_main\\img')),
            ],
        ),
    ]