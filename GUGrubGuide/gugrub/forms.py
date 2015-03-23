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
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(EateryReviewForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Review
        fields = ('title', 'description', 'qualityRating', 'valueRating', 'atmosphereRating', 'serviceRating', 'recommendRating',
            'picture')
        widgets = {
            'qualityRating': RadioSelect,
            'valueRating': RadioSelect,
            'atmosphereRating': RadioSelect,
            'serviceRating': RadioSelect,
            'recommendRating': RadioSelect,
        }


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