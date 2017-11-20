# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-09-19 11:26
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0034_pricepdf'),
    ]

    operations = [
        migrations.CreateModel(
            name='FACTORS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_factors', models.CharField(blank=True, choices=[('1', 'Женский фактор'), ('2', 'Мужской фактор')], max_length=255, verbose_name='Фактор')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Текст')),
            ],
            options={
                'verbose_name_plural': 'Факторы',
            },
        ),
    ]
