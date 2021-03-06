# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-28 07:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='description',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='name',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='crt_dt',
            field=models.DateField(default=datetime.datetime(2017, 10, 28, 7, 16, 39, 517355, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='exp_dt',
            field=models.DateField(default=datetime.datetime(2017, 11, 4, 7, 16, 39, 517355, tzinfo=utc)),
        ),
    ]
