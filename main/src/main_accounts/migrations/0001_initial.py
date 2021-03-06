# Generated by Django 3.0.8 on 2021-02-16 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='account_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mhi_id', models.CharField(blank=True, max_length=12, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('picture_file', models.CharField(blank=True, max_length=15, null=True)),
                ('access', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'verbose_name_plural': 'Accounts',
            },
        ),
    ]
