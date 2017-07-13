# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-08 22:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StoreBase', '0007_auto_20170706_2227'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StoreId', models.IntegerField(blank=True, null=True, unique=True)),
                ('StoreLogoImage', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StoreTimings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StoreId', models.IntegerField(blank=True, null=True, unique=True)),
                ('MondayOpeningTime', models.TimeField(blank=True, null=True)),
                ('TuesdayOpeningTime', models.TimeField(blank=True, null=True)),
                ('WednesdayOpeningTime', models.TimeField(blank=True, null=True)),
                ('ThursdayOpeningTime', models.TimeField(blank=True, null=True)),
                ('FridayOpeningTime', models.TimeField(blank=True, null=True)),
                ('SaturdayOpeningTime', models.TimeField(blank=True, null=True)),
                ('SundayOpeningTime', models.TimeField(blank=True, null=True)),
                ('MondayClosingTime', models.TimeField(blank=True, null=True)),
                ('TuesdayClosingTime', models.TimeField(blank=True, null=True)),
                ('WednesdayClosingTime', models.TimeField(blank=True, null=True)),
                ('ThursdayClosingTime', models.TimeField(blank=True, null=True)),
                ('FridayClosingTime', models.TimeField(blank=True, null=True)),
                ('SaturdayClosingTime', models.TimeField(blank=True, null=True)),
                ('SundayClosingTime', models.TimeField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='store',
            name='ClosingTime',
        ),
        migrations.RemoveField(
            model_name='store',
            name='OpeningTime',
        ),
        migrations.AddField(
            model_name='store',
            name='StoreLogo',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]