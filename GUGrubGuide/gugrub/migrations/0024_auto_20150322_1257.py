# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('gugrub', '0023_auto_20150322_0212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='atmosphereRating',
            field=models.IntegerField(choices=[(1, b'One'), (2, b'Two'), (3, b'Three'), (4, b'Four'), (5, b'Five')], validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='review',
            name='qualityRating',
            field=models.IntegerField(choices=[(1, b'One'), (2, b'Two'), (3, b'Three'), (4, b'Four'), (5, b'Five')], validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='review',
            name='recommendRating',
            field=models.IntegerField(choices=[(1, b'One'), (2, b'Two'), (3, b'Three'), (4, b'Four'), (5, b'Five')], validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='review',
            name='serviceRating',
            field=models.IntegerField(choices=[(1, b'One'), (2, b'Two'), (3, b'Three'), (4, b'Four'), (5, b'Five')], validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='review',
            name='valueRating',
            field=models.IntegerField(choices=[(1, b'One'), (2, b'Two'), (3, b'Three'), (4, b'Four'), (5, b'Five')], validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
    ]
