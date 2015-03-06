# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gugrub', '0018_auto_20150306_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='finalRating',
            field=models.DecimalField(default=0, help_text=b'(updated on save)', max_digits=2, decimal_places=1),
        ),
    ]
