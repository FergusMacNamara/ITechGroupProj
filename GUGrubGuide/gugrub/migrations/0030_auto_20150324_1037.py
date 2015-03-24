# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gugrub', '0029_auto_20150324_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eatery',
            name='picture',
            field=models.ImageField(upload_to=b'eatery_images', blank=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='description',
            field=models.TextField(max_length=400, null=True, blank=True),
        ),
    ]
