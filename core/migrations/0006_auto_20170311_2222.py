# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-11 22:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20170311_1734'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['category'], 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='phrase',
            options={'ordering': ['phrase']},
        ),
        migrations.AlterModelOptions(
            name='translation',
            options={'ordering': ['translation']},
        ),
        migrations.AlterModelOptions(
            name='word',
            options={'ordering': ['word']},
        ),
    ]
