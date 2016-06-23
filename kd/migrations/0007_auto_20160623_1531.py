# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-23 15:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('kd', '0006_auto_20160623_0454'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 6, 23, 15, 31, 5, 760698, tzinfo=utc), verbose_name='\u4e0b\u5355\u65f6\u95f4'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='valid',
            field=models.CharField(max_length=10, null=True, verbose_name='\u9a8c\u8bc1'),
        ),
    ]
