# Generated by Django 2.2.5 on 2020-06-25 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrg_hr_ref', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='projectcode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectcode', models.CharField(max_length=3)),
                ('projectcodedesc', models.CharField(blank=True, max_length=50, null=True)),
                ('projectname', models.TextField(blank=True, null=True)),
                ('projectsupervisor', models.CharField(blank=True, max_length=50, null=True)),
                ('startdate', models.DateField(blank=True, null=True)),
                ('enddate', models.DateField(blank=True, null=True)),
                ('isactive', models.IntegerField(blank=True, null=True)),
                ('multicharge', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
