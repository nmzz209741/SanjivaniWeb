# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-12 02:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20170812_0152'),
    ]

    operations = [
        migrations.CreateModel(
            name='purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('billno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.bill')),
                ('medid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.medicine')),
            ],
        ),
    ]