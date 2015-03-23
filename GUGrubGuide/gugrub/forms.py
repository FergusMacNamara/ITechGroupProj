__author__ = 'Fergus'

from django import forms
from gugrub.models import Review, Eatery
from django.contrib.auth.models import User

from django.forms.fields import ChoiceField
from django.forms.fields import MultipleChoiceField
from django.forms.widgets import RadioSelect
from django.forms.widgets import CheckboxSelectMultiple
from django.forms.extras.widgets import SelectDateWidget


class EateryReviewForm(forms.ModelForm):
    CHOICES = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'))
    date = forms.DateTimeInput
    title = forms.CharField(max_length=256, help_text="Please enter a title for your review.")
    description = forms.CharField(widget=forms.Textarea, help_text="Please describe your experience.")
    qualityRating = forms.ChoiceField(choices=CHOICES, widget=RadioSelect,
                                      help_text="How would you rate the quality of the food/drink?", )
    valueRating = forms.ChoiceField(choices=CHOICES, widget=RadioSelect,
                                    help_text="How would you rate the value of the food/drink?", )
    atmosphereRating = forms.ChoiceField(choices=CHOICES, widget=RadioSelect,
                                         help_text="How would you rate the atmosphere?", )
    serviceRating = forms.ChoiceField(choices=CHOICES, widget=RadioSelect,
                                      help_text="How would you rate the service?", )
    recommendRating = forms.ChoiceField(choices=CHOICES, widget=RadioSelect,
                                        help_text="How likely are you to recommend it to another student?", )
    picture = forms.FileField(label='Upload an Image', help_text="Would you like to upload an image?")

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(EateryReviewForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Review
        fields = (
            'title', 'description', 'qualityRating', 'valueRating', 'atmosphereRating', 'serviceRating', 'recommendRating',
            'picture')


class NewReviewForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(NewReviewForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Review
        fields = ('eatery', 'title', 'description', 'qualityRating', 'valueRating', 'atmosphereRating', 'serviceRating',
                  'recommendRating', 'picture')
        widgets = {
            'qualityRating': RadioSelect,
            'valueRating': RadioSelect,
            'atmosphereRating': RadioSelect,
            'serviceRating': RadioSelect,
            'recommendRating': RadioSelect,
        }


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')