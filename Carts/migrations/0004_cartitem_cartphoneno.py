# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-13 13:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Carts', '0003_auto_20170613_0252'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='CartPhoneNo',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
