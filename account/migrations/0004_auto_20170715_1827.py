# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-15 12:42
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_batchdata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batchdata',
            name='expdate',
        ),
        migrations.AddField(
            model_name='batchdata',
            name='exptag_validator',
            field=models.CharField(default='2017/09', max_length=8, validators=[django.core.validators.RegexValidator(message='Date doesnt comply', regex='((20)(1([2-9])|([2-9])([0-9])))/((0[1-9])|(1[0-2]))')]),
        ),
    ]