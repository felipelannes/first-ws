# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-01-19 01:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ASV_Vessel',
            fields=[
                ('ASV_Project_Number', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=32, unique=True)),
                ('Description', models.TextField(blank=True)),
                ('Mass', models.FloatField(null=True)),
                ('LCG', models.FloatField(null=True)),
                ('TCG', models.FloatField(null=True)),
                ('VCG', models.FloatField(null=True)),
                ('Creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Modification_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bounding_Box',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('X_aft', models.FloatField()),
                ('X_forward', models.FloatField()),
                ('Y_starboard', models.FloatField()),
                ('Y_portside', models.FloatField()),
                ('Z_bottom', models.FloatField()),
                ('Z_up', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Group_System',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_GS', models.IntegerField()),
                ('Mass', models.FloatField(default=0)),
                ('LCG', models.FloatField(default=0)),
                ('TCG', models.FloatField(default=0)),
                ('VCG', models.FloatField(default=0)),
                ('ID_ASV', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weightsheet.ASV_Vessel')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Part_Name', models.CharField(max_length=32)),
                ('Quantity', models.FloatField()),
                ('Mass', models.FloatField()),
                ('LCG', models.FloatField()),
                ('TCG', models.FloatField()),
                ('VCG', models.FloatField()),
                ('Description', models.TextField(blank=True)),
                ('ID_Item', models.IntegerField()),
                ('ASV_Item', models.BooleanField()),
                ('Global_Group', models.IntegerField()),
                ('ID_ASV', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weightsheet.ASV_Vessel')),
                ('ID_GS', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weightsheet.Group_System')),
            ],
        ),
    ]
