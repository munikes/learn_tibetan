# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocabulary_game', '0003_category_language_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('score', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
    ]
