# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-24 17:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/static/upload/blog/', verbose_name='Главная картинка'),
        ),
    ]
