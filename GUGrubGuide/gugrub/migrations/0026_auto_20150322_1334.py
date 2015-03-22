# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('gugrub', '0025_auto_20150322_1320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='qualityRating_score',
        ),
        migrations.RemoveField(
            model_name='review',
            name='qualityRating_votes',
        ),
        migrations.AddField(
            model_name='review',
            name='atmosphereRating',
            field=models.IntegerField(default=0, choices=[(1, b'One'), (2, b'Two'), (3, b'Three'), (4, b'Four'), (5, b'Five')], validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='review',
            name='qualityRating',
            field=models.IntegerField(default=0, choices=[(1, b'One'), (2, b'Two'), (3, b'Three'), (4, b'Four'), (5, b'Five')], validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='review',
            name='recommendRating',
            field=models.IntegerField(default=0, choices=[(1, b'One'), (2, b'Two'), (3, b'Three'), (4, b'Four'), (5, b'Five')], validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='review',
            name='serviceRating',
            field=models.IntegerField(default=0, choices=[(1, b'One'), (2, b'Two'), (3, b'Three'), (4, b'Four'), (5, b'Five')], validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='review',
            name='valueRating',
            field=models.IntegerField(default=0, choices=[(1, b'One'), (2, b'Two'), (3, b'Three'), (4, b'Four'), (5, b'Five')], validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
            preserve_default=True,
        ),
    ]
