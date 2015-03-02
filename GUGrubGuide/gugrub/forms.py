__author__ = 'Fergus'

from django import forms
from gugrub.models import Review, Eatery

class ReviewForm(forms.ModelForm):
    eatery = forms.ModelChoiceField(queryset=Eatery.objects.all(), help_text="Please enter the eatery name.")
    title = forms.CharField(max_length=256, help_text="Please enter a title for your review.")
    description = forms.CharField(widget = forms.Textarea, help_text="Please describe your experience.")
    qualityRating = forms.IntegerField(help_text="How would you rate the quality of the food/drink?", max_value=5, min_value=0)
    valueRating = forms.IntegerField(help_text="How would you rate the value of the food/drink?", max_value=5, min_value=0)
    atmosphereRating = forms.IntegerField(help_text="How would you rate the atmosphere?", max_value=5, min_value=0)
    serviceRating = forms.IntegerField(help_text="How would you rate the service?", max_value=5, min_value=0)
    recommendRating = forms.IntegerField(help_text="How likely are you to recommend it to another student?", max_value=5, min_value=0)
    picture = forms.FileField(label='Upload an Image', help_text="Would you like to upload an image?")

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Review
        fields = ('title',)