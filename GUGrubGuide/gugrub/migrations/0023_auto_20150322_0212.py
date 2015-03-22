# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('gugrub', '0022_auto_20150321_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='atmosphereRating',
            field=models.IntegerField(default=0, choices=[(b'1', b'One'), (b'2', b'Two'), (b'3', b'Three'), (b'4', b'Four'), (b'5', b'Five')], validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='review',
            name='qualityRating',
            field=models.IntegerField(default=0, choices=[(b'1', b'One'), (b'2', b'Two'), (b'3', b'Three'), (b'4', b'Four'), (b'5', b'Five')], validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='review',
            name='recommendRating',
            field=models.IntegerField(default=0, choices=[(b'1', b'One'), (b'2', b'Two'), (b'3', b'Three'), (b'4', b'Four'), (b'5', b'Five')], validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='review',
            name='serviceRating',
            field=models.IntegerField(default=0, choices=[(b'1', b'One'), (b'2', b'Two'), (b'3', b'Three'), (b'4', b'Four'), (b'5', b'Five')], validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='review',
            name='valueRating',
            field=models.IntegerField(default=0, choices=[(b'1', b'One'), (b'2', b'Two'), (b'3', b'Three'), (b'4', b'Four'), (b'5', b'Five')], validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
    ]
