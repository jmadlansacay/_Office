# Generated by Django 3.0.8 on 2021-03-16 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management_main', '0025_auto_20210315_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='title',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='managers',
            name='title',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
