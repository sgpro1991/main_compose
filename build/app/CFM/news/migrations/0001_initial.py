# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 14:00
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('description', models.CharField(max_length=255, verbose_name='Описание')),
                ('date_time', models.DateTimeField(auto_now_add=True, verbose_name='Дата время')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Текст')),
            ],
        ),
    ]
