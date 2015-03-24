# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gugrub', '0019_auto_20150306_1828'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eatery',
            old_name='averageatmosphereRating',
            new_name='averageAtmosphereRating',
        ),
        migrations.RenameField(
            model_name='eatery',
            old_name='averagequalityRating',
            new_name='averageQualityRating',
        ),
        migrations.RenameField(
            model_name='eatery',
            old_name='averagerecommendRating',
            new_name='averageRecommendRating',
        ),
        migrations.RenameField(
            model_name='eatery',
            old_name='averageserviceRating',
            new_name='averageServiceRating',
        ),
        migrations.RemoveField(
            model_name='eatery',
            name='averagevalueRating',
        ),
        migrations.AddField(
            model_name='eatery',
            name='averageValueRating',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
    ]
