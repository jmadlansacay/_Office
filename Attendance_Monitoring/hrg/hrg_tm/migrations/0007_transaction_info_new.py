# Generated by Django 2.2.5 on 2020-07-08 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrg_tm', '0006_transaction_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='transaction_info_new',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeeid', models.CharField(blank=True, max_length=4, null=True)),
                ('timesheetdate', models.DateField(blank=True, null=True)),
                ('halfday', models.IntegerField(blank=True, null=True)),
                ('reason', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
    ]