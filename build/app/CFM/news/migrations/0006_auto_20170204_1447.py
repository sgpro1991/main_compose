# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 14:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20170204_1436'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='date_time',
        ),
        migrations.AddField(
            model_name='news',
            name='date',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Дата'),
        ),
    ]
