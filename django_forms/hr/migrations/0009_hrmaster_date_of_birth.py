# Generated by Django 3.0.8 on 2020-09-30 09:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0008_hrmaster'),
    ]

    operations = [
        migrations.AddField(
            model_name='hrmaster',
            name='date_of_birth',
            field=models.DateField(default=datetime.date.today),
        ),
    ]