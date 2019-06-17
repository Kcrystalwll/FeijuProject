# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2019-05-29 18:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mygas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gs_meterinfo_csb',
            name='MeterTypeId',
        ),
        migrations.RemoveField(
            model_name='gs_meterinfo_ic',
            name='MeterTypeId',
        ),
        migrations.RemoveField(
            model_name='gs_meterinfo_msb',
            name='MeterTypeId',
        ),
        migrations.RemoveField(
            model_name='gs_meterinfo_xzy',
            name='MeterTypeId',
        ),
        migrations.RemoveField(
            model_name='gs_metertypeinfo',
            name='ManufactureName',
        ),
        migrations.RemoveField(
            model_name='gs_metertypeinfo',
            name='user',
        ),
        migrations.DeleteModel(
            name='Meter_Result',
        ),
        migrations.DeleteModel(
            name='Meter_Result_Record',
        ),
        migrations.DeleteModel(
            name='Meter_Test',
        ),
        migrations.DeleteModel(
            name='MeterPlat',
        ),
        migrations.DeleteModel(
            name='PlanInfo',
        ),
        migrations.DeleteModel(
            name='GS_MeterInfo_CSB',
        ),
        migrations.DeleteModel(
            name='GS_MeterInfo_IC',
        ),
        migrations.DeleteModel(
            name='GS_MeterInfo_MSB',
        ),
        migrations.DeleteModel(
            name='GS_MeterInfo_XZY',
        ),
        migrations.DeleteModel(
            name='GS_MeterTypeInfo',
        ),
        migrations.DeleteModel(
            name='Manufacture',
        ),
    ]
