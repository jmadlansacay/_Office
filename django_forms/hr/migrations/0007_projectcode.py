# Generated by Django 3.0.8 on 2020-09-30 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0006_delete_projectcode'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_description', models.CharField(max_length=50)),
                ('projectname', models.TextField()),
                ('projectsupervisor', models.CharField(blank=True, max_length=50, null=True)),
                ('startdate', models.DateField(blank=True, null=True)),
                ('enddate', models.DateField(blank=True, null=True)),
                ('isactive', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
