from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Eatery(models.Model):
        name = models.CharField(max_length=128, unique=True)
        picture = models.ImageField(upload_to='eatery_images', blank=True)
        location = models.CharField(max_length=256)
        description = models.TextField()
        url = models.URLField()
        slug = models.SlugField(unique=True)

        def save(self, *args, **kwargs):
                self.slug = slugify(self.name)
                super(Eatery, self).save(*args, **kwargs)

        def __unicode__(self):
                return self.name

        class Meta:
            verbose_name_plural = "Eateries"


class Review(models.Model):
        eatery = models.ForeignKey(Eatery)
        reviewer = models.ForeignKey(User)
        title = models.CharField(max_length=128)
        description = models.TextField()
        qualityRating = models.PositiveIntegerField(default=0)
        valueRating = models.PositiveIntegerField(default=0)
        atmosphereRating = models.PositiveIntegerField(default=0)
        serviceRating = models.PositiveIntegerField(default=0)
        recommendRating = models.PositiveIntegerField(default=0)
        picture = models.ImageField(upload_to='review_images', blank=True)


        def __unicode__(self):
            return self.title