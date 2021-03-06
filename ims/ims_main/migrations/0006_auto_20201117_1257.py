# Generated by Django 3.0.8 on 2020-11-17 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ims_main', '0005_tbl_icn'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_icn',
            name='designer',
            field=models.ForeignKey(blank=True, limit_choices_to={'user_access': 9}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='designer', to='ims_main.user_detail'),
        ),
        migrations.AddField(
            model_name='tbl_icn',
            name='line_id',
            field=models.CharField(default='123', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tbl_icn',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='location', to='ims_main.user_detail'),
        ),
        migrations.AlterField(
            model_name='tbl_icn',
            name='area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ims_main.ref_area'),
        ),
    ]
