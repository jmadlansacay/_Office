# Generated by Django 2.2.12 on 2020-09-21 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrg_hr', '0011_user_detail_remarks'),
    ]

    operations = [
        migrations.CreateModel(
            name='intro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeeid', models.CharField(blank=True, max_length=4, null=True)),
                ('msg', models.TextField(blank=True)),
            ],
        ),
    ]