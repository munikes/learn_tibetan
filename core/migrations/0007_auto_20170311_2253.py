# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-11 22:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20170311_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='translation',
            name='translation',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterUniqueTogether(
            name='translation',
            unique_together=set([('translation', 'language_code')]),
        ),
    ]
