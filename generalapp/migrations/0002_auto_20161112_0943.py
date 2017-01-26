# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-12 15:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generalapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='tipo_consulta',
            field=models.CharField(blank=True, choices=[('PRV', 'Primera vez'), ('SUB', 'Subsecuente')], default='PRV', max_length=50),
        ),
    ]
