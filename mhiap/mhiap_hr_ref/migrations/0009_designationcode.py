# Generated by Django 3.0.8 on 2020-09-29 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mhiap_hr_ref', '0008_projectcode'),
    ]

    operations = [
        migrations.CreateModel(
            name='DesignationCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=150)),
                ('designation_group', models.CharField(max_length=150)),
            ],
        ),
    ]
