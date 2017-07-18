# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-18 19:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BatchBase', '0006_batch_shopperid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batch',
            name='OrderId',
        ),
        migrations.AddField(
            model_name='batch',
            name='Size',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]