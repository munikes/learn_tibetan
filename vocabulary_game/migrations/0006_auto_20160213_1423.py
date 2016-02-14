# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocabulary_game', '0005_auto_20160210_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='translation',
            field=models.ManyToManyField(related_name='word_translation', to='vocabulary_game.Translation'),
        ),
    ]
