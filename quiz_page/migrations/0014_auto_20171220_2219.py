# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-20 16:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_page', '0013_auto_20171220_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='crt_dt',
            field=models.DateField(default=datetime.datetime(2017, 12, 20, 16, 49, 41, 934412, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='exp_dt',
            field=models.DateField(default=datetime.datetime(2017, 12, 27, 16, 49, 41, 934412, tzinfo=utc)),
        ),
    ]
