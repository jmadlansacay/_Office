# Generated by Django 3.0.8 on 2021-01-20 01:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management_main', '0002_employeehours'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeehours',
            old_name='nickname',
            new_name='employee',
        ),
        migrations.AlterUniqueTogether(
            name='employeehours',
            unique_together={('employee', 'year')},
        ),
    ]
