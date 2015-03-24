# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gugrub', '0028_auto_20150322_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eatery',
            name='picture',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
    ]
