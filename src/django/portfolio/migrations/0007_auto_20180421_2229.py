# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-21 22:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_auto_20180421_0032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='date',
        ),
        migrations.AddField(
            model_name='transaction',
            name='currency',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='time',
            field=models.TimeField(verbose_name='Time'),
        ),
    ]
