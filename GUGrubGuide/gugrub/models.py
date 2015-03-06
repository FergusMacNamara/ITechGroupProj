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
        averagequalityRating = models.FloatField(default=0)
        averagevalueRating = models.FloatField(default=0)
        averageatmosphereRating = models.FloatField(default=0)
        averageserviceRating = models.FloatField(default=0)
        averagerecommendRating = models.FloatField(default=0)
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
        date = models.DateTimeField(default=datetime.now, blank=True)
        title = models.CharField(max_length=128)
        description = models.TextField()
        qualityRating = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
        valueRating = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
        atmosphereRating = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
        serviceRating = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
        recommendRating = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
        picture = models.ImageField(upload_to='review_images', blank=True)
        finalRating = models.DecimalField(default=0, max_digits=2, decimal_places=1, help_text="(updated on save)")


        def save(self, *args, **kwargs):
            self.finalRating = (self.qualityRating + self.valueRating + self.atmosphereRating + self.serviceRating + self.recommendRating)/5
            super(Review, self).save(*args, **kwargs)

        def __unicode__(self):
            return self.title