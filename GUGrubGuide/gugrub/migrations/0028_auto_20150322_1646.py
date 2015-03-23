# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gugrub', '0027_auto_20150322_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='atmosphereRating',
            field=models.IntegerField(default=0, choices=[(1, b'One'), (2, b'Two'), (3, b'Three'), (4, b'Four'), (5, b'Five')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='qualityRating',
            field=models.IntegerField(default=0, choices=[(1, b'One'), (2, b'Two'), (3, b'Three'), (4, b'Four'), (5, b'Five')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='recommendRating',
            field=models.IntegerField(default=0, choices=[(1, b'One'), (2, b'Two'), (3, b'Three'), (4, b'Four'), (5, b'Five')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='serviceRating',
            field=models.IntegerField(default=0, choices=[(1, b'One'), (2, b'Two'), (3, b'Three'), (4, b'Four'), (5, b'Five')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='valueRating',
            field=models.IntegerField(default=0, choices=[(1, b'One'), (2, b'Two'), (3, b'Three'), (4, b'Four'), (5, b'Five')]),
        ),
    ]
