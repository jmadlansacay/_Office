# Generated by Django 3.0.8 on 2020-11-17 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ims_main', '0002_user_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_detail',
            name='pic',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]