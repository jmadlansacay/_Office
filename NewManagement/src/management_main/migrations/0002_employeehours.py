# Generated by Django 3.0.8 on 2021-01-20 00:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management_main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeHours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('jan_hrs', models.FloatField(default=0)),
                ('feb_hrs', models.FloatField(default=0)),
                ('mar_hrs', models.FloatField(default=0)),
                ('apr_hrs', models.FloatField(default=0)),
                ('may_hrs', models.FloatField(default=0)),
                ('jun_hrs', models.FloatField(default=0)),
                ('jul_hrs', models.FloatField(default=0)),
                ('aug_hrs', models.FloatField(default=0)),
                ('sep_hrs', models.FloatField(default=0)),
                ('oct_hrs', models.FloatField(default=0)),
                ('nov_hrs', models.FloatField(default=0)),
                ('dec_hrs', models.FloatField(default=0)),
                ('nickname', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='management_main.Employees')),
            ],
            options={
                'verbose_name': 'No of Employee Man Hour',
                'unique_together': {('nickname', 'year')},
            },
        ),
    ]
