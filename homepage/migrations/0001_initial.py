# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-03 18:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_no', models.TextField(max_length=20)),
                ('enter_date', models.DateField(default=datetime.datetime(2017, 11, 3, 18, 18, 51, 615817, tzinfo=utc))),
            ],
        ),
    ]
