# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-07 00:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopperBase', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopper',
            name='PhoneNo',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]