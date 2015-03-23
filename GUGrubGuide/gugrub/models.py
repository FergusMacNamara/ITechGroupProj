from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from datetime import datetime

class Eatery(models.Model):
        name = models.CharField(max_length=128, unique=True)
        picture = models.ImageField(upload_to='eatery_images', blank=True)
        location = models.CharField(max_length=256)
        description = models.TextField()
        url = models.URLField()
        averageRating = models.FloatField(default=0)
        averageQualityRating = models.FloatField(default=0)
        averageValueRating = models.FloatField(default=0)
        averageAtmosphereRating = models.FloatField(default=0)
        averageServiceRating = models.FloatField(default=0)
        averageRecommendRating = models.FloatField(default=0)
        slug = models.SlugField(unique=True)

        def save(self, *args, **kwargs):
                self.slug = slugify(self.name)
                super(Eatery, self).save(*args, **kwargs)

        def __unicode__(self):
                return self.name

        class Meta:
            verbose_name_plural = "Eateries"


class Review(models.Model):

        CHOICES = ((1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five'))

        eatery = models.ForeignKey(Eatery)
        reviewer = models.ForeignKey(User)
        date = models.DateTimeField(default=datetime.now, blank=True)
        title = models.CharField(max_length=128)
        description = models.TextField(blank=True, null=True)
        qualityRating = models.IntegerField(choices=CHOICES, default=0)
        valueRating = models.IntegerField(choices=CHOICES, default=0)
        atmosphereRating = models.IntegerField(choices=CHOICES, default=0)
        serviceRating = models.IntegerField(choices=CHOICES, default=0)
        recommendRating = models.IntegerField(choices=CHOICES, default=0)
        picture = models.ImageField(upload_to='review_images', blank=True)
        finalRating = models.DecimalField(default=0, max_digits=2, decimal_places=1, help_text="(updated on save)")


        def save(self, *args, **kwargs):
            self.finalRating = (self.qualityRating + self.valueRating + self.atmosphereRating + self.serviceRating + self.recommendRating)/5
            super(Review, self).save(*args, **kwargs)

        def __unicode__(self):
            return self.title