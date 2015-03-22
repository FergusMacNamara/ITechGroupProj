# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gugrub', '0024_auto_20150322_1257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='atmosphereRating',
        ),
        migrations.RemoveField(
            model_name='review',
            name='qualityRating',
        ),
        migrations.RemoveField(
            model_name='review',
            name='recommendRating',
        ),
        migrations.RemoveField(
            model_name='review',
            name='serviceRating',
        ),
        migrations.RemoveField(
            model_name='review',
            name='valueRating',
        ),
        migrations.AddField(
            model_name='review',
            name='qualityRating_score',
            field=models.IntegerField(default=0, editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='review',
            name='qualityRating_votes',
            field=models.PositiveIntegerField(default=0, editable=False, blank=True),
            preserve_default=True,
        ),
    ]
