# Generated by Django 2.2.5 on 2020-07-03 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrg_hr', '0008_user_detail_user_access'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_detail',
            name='user_access',
        ),
    ]
