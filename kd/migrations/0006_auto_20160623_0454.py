# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-23 04:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kd', '0005_auto_20160621_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shipping_user_id',
            field=models.CharField(max_length=50, null=True, verbose_name='\u5bc4\u9001\u4eba\u90ae\u7bb1'),
        ),
    ]