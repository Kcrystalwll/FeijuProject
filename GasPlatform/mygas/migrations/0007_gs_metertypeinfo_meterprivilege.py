# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2019-06-15 19:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mygas', '0006_auto_20190615_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='gs_metertypeinfo',
            name='MeterPrivilege',
            field=models.CharField(default='0', max_length=1),
        ),
    ]
