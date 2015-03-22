# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('gugrub', '0021_auto_20150321_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='atmosphereRating',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='review',
            name='recommendRating',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='review',
            name='serviceRating',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='review',
            name='valueRating',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
            preserve_default=True,
        ),
    ]
