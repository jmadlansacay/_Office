# Generated by Django 3.0.8 on 2020-11-22 01:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ims_main', '0011_tbl_icn_latest_issue_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_note1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rev0', models.DateField(blank=True, null=True)),
                ('rev1', models.DateField(blank=True, null=True)),
                ('rev2', models.DateField(blank=True, null=True)),
                ('rev3', models.DateField(blank=True, null=True)),
                ('rev4', models.DateField(blank=True, null=True)),
                ('rev5', models.DateField(blank=True, null=True)),
                ('rev6', models.DateField(blank=True, null=True)),
                ('icn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ims_main.tbl_icn')),
            ],
        ),
    ]