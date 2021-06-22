# Generated by Django 3.0.8 on 2021-06-07 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eval_app', '0017_auto_20210607_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='dispatch_africa',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='dispatch_bangladesh',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='dispatch_japan',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='dispatch_north_europe',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='dispatch_philippines',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='dispatch_russia',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='dispatch_singapore',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='dispatch_us_canada',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='fairness_for_all',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='rule_on_the_company',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='share_knowledge',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='terms_of_salary',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='think_yourself',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=1, null=True),
        ),
    ]