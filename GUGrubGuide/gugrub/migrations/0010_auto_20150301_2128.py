# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gugrub', '0009_auto_20150301_2105'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='placetoeat',
            options={'verbose_name_plural': 'PlacesToEat'},
        ),
    ]
