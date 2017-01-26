# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-24 03:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generalapp', '0003_auto_20161117_1120'),
    ]

    operations = [
        migrations.CreateModel(
            name='Forma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_forma', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Via',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_via', models.CharField(max_length=200)),
            ],
        ),
    ]