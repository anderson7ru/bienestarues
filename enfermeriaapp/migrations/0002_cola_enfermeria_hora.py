# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-30 00:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enfermeriaapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cola_enfermeria',
            name='hora',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
