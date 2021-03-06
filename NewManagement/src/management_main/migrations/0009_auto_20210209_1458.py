# Generated by Django 3.0.8 on 2021-02-09 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management_main', '0008_auto_20210209_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='covid',
            name='active_cases',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='covid',
            name='bed_occ',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='covid',
            name='bed_occpuancy',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='covid',
            name='bed_vac',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='covid',
            name='died',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='covid',
            name='icu_occ',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='covid',
            name='icu_vac',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='covid',
            name='isolation_occ',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='covid',
            name='isolation_vac',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='covid',
            name='recovered',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='covid',
            name='ventilator_occ',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='covid',
            name='ventilator_vac',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='covid',
            name='ward_occ',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='covid',
            name='ward_vac',
            field=models.IntegerField(default=0),
        ),
    ]
