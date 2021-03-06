# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-01 15:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0010_auto_20180101_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentresponse',
            name='attempted_date',
            field=models.DateField(default=datetime.datetime(2018, 1, 1, 15, 42, 33, 559148, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='studentresponse',
            name='time_remaining',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='students',
            name='join_date',
            field=models.DateField(default=datetime.datetime(2018, 1, 1, 15, 42, 33, 559148, tzinfo=utc)),
        ),
    ]
