# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-11-08 08:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='name',
            field=models.CharField(default='MilkBook', max_length=32),
        ),
        migrations.AddField(
            model_name='movie',
            name='name',
            field=models.CharField(default='MilkMovie', max_length=32),
        ),
        migrations.AddField(
            model_name='music',
            name='name',
            field=models.CharField(default='MilkMusic', max_length=32),
        ),
    ]
