# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceToEat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('picture', models.ImageField(upload_to=b'placeToEat_images', blank=True)),
                ('location', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('url', models.URLField()),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('picture', models.ImageField(upload_to=b'review_images', blank=True)),
                ('qualityRating', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(15), django.core.validators.MinValueValidator(0)])),
                ('valueRating', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(15), django.core.validators.MinValueValidator(0)])),
                ('atmosphereRating', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(15), django.core.validators.MinValueValidator(0)])),
                ('serviceRating', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(15), django.core.validators.MinValueValidator(0)])),
                ('recommendRating', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(15), django.core.validators.MinValueValidator(0)])),
                ('placeToEat', models.ForeignKey(to='gugrub.PlaceToEat')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('picture', models.ImageField(upload_to=b'profile_images', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='review',
            name='reviewer',
            field=models.ForeignKey(to='gugrub.UserProfile'),
            preserve_default=True,
        ),
    ]
