# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-27 02:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20180226_2318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='experience',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='skill',
        ),
        migrations.AddField(
            model_name='skill',
            name='skills',
            field=models.TextField(null=True),
        ),
    ]