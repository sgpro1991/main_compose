# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-03-17 10:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0038_auto_20190317_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recordonline',
            name='city',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='филиал'),
        ),
    ]
