# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-01 15:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0009_auto_20171227_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentresponse',
            name='attempted_date',
            field=models.DateField(default=datetime.datetime(2018, 1, 1, 15, 41, 32, 63683, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='studentresponse',
            name='time_remaining',
            field=models.CharField(default='0', max_length=20),
        ),
        migrations.AlterField(
            model_name='students',
            name='join_date',
            field=models.DateField(default=datetime.datetime(2018, 1, 1, 15, 41, 32, 63683, tzinfo=utc)),
        ),
    ]
