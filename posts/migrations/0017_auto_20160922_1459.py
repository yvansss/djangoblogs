# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-22 11:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0016_auto_20160922_1457'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='pub',
        ),
        migrations.AddField(
            model_name='post',
            name='pubs',
            field=models.DateField(default=datetime.datetime(2016, 9, 22, 11, 59, 27, 839000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
