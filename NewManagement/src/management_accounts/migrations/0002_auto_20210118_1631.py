# Generated by Django 3.0.8 on 2021-01-18 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management_accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]