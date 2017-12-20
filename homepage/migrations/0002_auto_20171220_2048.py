# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-20 15:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='enter_date',
        ),
        migrations.AddField(
            model_name='students',
            name='dob',
            field=models.DateField(default='1899-12-31'),
        ),
        migrations.AddField(
            model_name='students',
            name='email',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='students',
            name='is_member',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AddField(
            model_name='students',
            name='join_date',
            field=models.DateField(default=datetime.datetime(2017, 12, 20, 15, 18, 15, 880958, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='students',
            name='location',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='students',
            name='mother_name',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='students',
            name='name',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='students',
            name='parent_contact',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='students',
            name='school',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='students',
            name='volunteer',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AddField(
            model_name='students',
            name='zone',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='students',
            name='mobile_no',
            field=models.TextField(default=None, max_length=20),
        ),
    ]