# Generated by Django 3.0.8 on 2021-05-20 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='wfh_items_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_description', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Item Category',
            },
        ),
    ]
