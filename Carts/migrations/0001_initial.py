# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-14 11:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('UserBase', '0001_initial'),
        ('Products', '0001_initial'),
        ('OrderBase', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Total', models.FloatField(blank=True, default=0.0)),
                ('UserPhone', models.BigIntegerField(blank=True, null=True, unique=True)),
                ('DeliveryCharges', models.FloatField(blank=True, default=0.0)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('Active', models.BooleanField(default=True)),
                ('Username', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='UserBase.User')),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CartPhoneNo', models.BigIntegerField(blank=True, null=True)),
                ('RemovedFromCart', models.BooleanField(default=False)),
                ('IsOrdered', models.BooleanField(default=False)),
                ('Quantity', models.FloatField(blank=True, default=1.0)),
                ('SubTotal', models.FloatField(blank=True, null=True)),
                ('Notes', models.TextField(blank=True, null=True)),
                ('Active', models.BooleanField(default=True)),
                ('Cart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='carts', to='Carts.Cart')),
                ('Item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Products.Product')),
                ('OrderId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='OrderBase.Order')),
            ],
        ),
    ]
