# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-12-28 13:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weightsheet', '0005_auto_20171220_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='Description',
            field=models.TextField(blank=True),
        ),
    ]
