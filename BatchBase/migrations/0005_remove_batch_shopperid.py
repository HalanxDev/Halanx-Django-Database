# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-15 11:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BatchBase', '0004_auto_20170715_1641_squashed_0005_auto_20170715_1643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batch',
            name='ShopperId',
        ),
    ]
