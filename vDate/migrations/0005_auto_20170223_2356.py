# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-23 18:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vDate', '0004_auto_20170220_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relation',
            name='boy',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='vDate.Girl'),
        ),
    ]