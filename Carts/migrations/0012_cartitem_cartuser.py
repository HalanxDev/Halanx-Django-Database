# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 12:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserBase', '0011_auto_20170624_0204'),
        ('Carts', '0011_cartitem_batchid'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='CartUser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='UserBase.User'),
        ),
    ]
