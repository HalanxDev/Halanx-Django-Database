# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-13 12:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OrderBase', '0002_auto_20170613_0252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='Items',
        ),
    ]