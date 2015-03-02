# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gugrub', '0010_auto_20150301_2128'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eatery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('picture', models.ImageField(upload_to=b'eatery_images', blank=True)),
                ('location', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('url', models.URLField()),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name_plural': 'Eateries',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='review',
            name='placeToEat',
        ),
        migrations.DeleteModel(
            name='PlaceToEat',
        ),
        migrations.AddField(
            model_name='review',
            name='eatery',
            field=models.ForeignKey(default=1, to='gugrub.Eatery'),
            preserve_default=False,
        ),
    ]
