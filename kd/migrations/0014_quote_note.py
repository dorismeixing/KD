# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-31 04:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kd', '0013_auto_20160731_0342'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='note',
            field=models.CharField(max_length=500, null=True, verbose_name='\u5907\u6ce8'),
        ),
    ]
