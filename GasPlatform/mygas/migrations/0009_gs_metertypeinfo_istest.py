# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2019-06-17 11:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mygas', '0008_auto_20190616_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='gs_metertypeinfo',
            name='IsTest',
            field=models.BooleanField(default=0),
        ),
    ]
