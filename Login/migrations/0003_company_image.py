# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-07 07:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0002_auto_20180129_1831'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='image',
            field=models.ImageField(default='', upload_to='images//%Y/%m/%d'),
            preserve_default=False,
        ),
    ]
