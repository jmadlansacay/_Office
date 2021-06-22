# Generated by Django 2.2.5 on 2020-06-26 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hrg_tm', '0002_delete_transacations'),
    ]

    operations = [
        migrations.CreateModel(
            name='transacations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeeid', models.CharField(blank=True, max_length=4, null=True)),
                ('employeetype', models.CharField(blank=True, max_length=2, null=True)),
                ('timesheetdate', models.DateField(blank=True, null=True)),
                ('inout', models.IntegerField(blank=True, null=True)),
                ('timepunch', models.TimeField(blank=True, null=True)),
                ('createdby', models.CharField(blank=True, max_length=50, null=True)),
                ('createddate', models.DateTimeField(blank=True, null=True)),
                ('machinename', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
