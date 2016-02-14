# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocabulary_game', '0004_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='name',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
