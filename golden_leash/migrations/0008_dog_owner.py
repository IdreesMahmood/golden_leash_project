# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-20 21:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('golden_leash', '0007_auto_20190320_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='golden_leash.UserProfile'),
        ),
    ]
