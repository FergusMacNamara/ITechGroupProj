# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gugrub', '0020_auto_20150317_1849'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='atmosphereRating',
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
    ]
