# Generated by Django 2.2.5 on 2020-07-03 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrg_hr', '0010_user_detail_user_access'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_detail',
            name='remarks',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
