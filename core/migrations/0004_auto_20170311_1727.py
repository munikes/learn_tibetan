# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-11 17:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20170311_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='pronunciation',
            field=models.FileField(blank=True, null=True, upload_to=b'pronunciations/'),
        ),
    ]
