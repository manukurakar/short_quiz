# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-28 07:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_page', '0006_auto_20171028_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='crt_dt',
            field=models.DateField(default=datetime.datetime(2017, 10, 28, 7, 22, 11, 734215, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='exp_dt',
            field=models.DateField(default=datetime.datetime(2017, 11, 4, 7, 22, 11, 734215, tzinfo=utc)),
        ),
    ]
