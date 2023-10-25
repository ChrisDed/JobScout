# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-28 18:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employers', '0010_auto_20180228_0624'),
        ('users', '0010_auto_20180227_0703'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='listings',
            field=models.ManyToManyField(related_name='resumes', to='employers.Listing'),
        ),
    ]