# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 12:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BatchBase', '0007_auto_20170719_0040'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='CentroidLatitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='batch',
            name='CentroidLongitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]