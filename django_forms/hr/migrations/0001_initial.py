# Generated by Django 3.0.8 on 2020-09-30 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CivilStatusCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('civilstatus', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
    ]
