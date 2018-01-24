# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-24 18:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0012_auto_20180124_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentresponse',
            name='attempted_date',
            field=models.DateField(default=datetime.datetime(2018, 1, 24, 18, 28, 18, 389828, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='students',
            name='join_date',
            field=models.DateField(default=datetime.datetime(2018, 1, 24, 18, 28, 18, 389828, tzinfo=utc)),
        ),
    ]