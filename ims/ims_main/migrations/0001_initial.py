# Generated by Django 3.0.8 on 2020-11-17 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ref_user_access',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_access_description', models.CharField(blank=True, max_length=20, null=True)),
                ('sort_order', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Reference User Access',
                'verbose_name_plural': 'Reference User Access',
            },
        ),
    ]
