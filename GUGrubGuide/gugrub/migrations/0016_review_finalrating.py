# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gugrub', '0015_auto_20150306_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='finalRating',
            field=models.IntegerField(default=0, help_text=b'(updated on save)'),
            preserve_default=False,
        ),
    ]
