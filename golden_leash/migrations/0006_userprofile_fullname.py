# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-20 17:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('golden_leash', '0005_auto_20190320_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='fullname',
            field=models.CharField(default='', max_length=128),
        ),
    ]
