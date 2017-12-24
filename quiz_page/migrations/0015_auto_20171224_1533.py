# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-24 10:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_page', '0014_auto_20171220_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='timer_sec',
            field=models.IntegerField(default=600),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='crt_dt',
            field=models.DateField(default=datetime.datetime(2017, 12, 24, 10, 3, 32, 601123, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='exp_dt',
            field=models.DateField(default=datetime.datetime(2017, 12, 31, 10, 3, 32, 601123, tzinfo=utc)),
        ),
    ]
