# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocabulary_game', '0002_auto_20160117_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='language_code',
            field=models.CharField(default=b'es', max_length=2, choices=[(b'es', b'Espa\xc3\xb1ol'), (b'en', b'English')]),
        ),
    ]
