# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-20 16:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_auto_20171220_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='dob',
            field=models.DateField(default='1899-12-31', null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='is_member',
            field=models.CharField(default=None, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='join_date',
            field=models.DateField(default=datetime.datetime(2017, 12, 20, 16, 23, 29, 826174, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='students',
            name='location',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='mobile_no',
            field=models.TextField(default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='mother_name',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='name',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='parent_contact',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='school',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='volunteer',
            field=models.CharField(default=None, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='zone',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]
