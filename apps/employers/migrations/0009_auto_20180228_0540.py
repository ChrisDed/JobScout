# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-28 05:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employers', '0008_remove_listing_job_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='job_decription',
            new_name='job_description',
        ),
    ]
