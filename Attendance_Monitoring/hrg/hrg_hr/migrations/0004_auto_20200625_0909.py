# Generated by Django 2.2.5 on 2020-06-25 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrg_hr', '0003_tblmaster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tblmaster',
            name='username',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
