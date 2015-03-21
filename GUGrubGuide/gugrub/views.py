from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from gugrub.models import Eatery, Review
from gugrub.forms import EateryReviewForm,NewReviewForm, UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Avg


def index(request):

    context_dict = {}

    eatery_list = Eatery.objects.order_by('averageRating')

    for eatery in eatery_list:
        reviews = Review.objects.filter(eatery=eatery)
        eatery.averageRating = reviews.aggregate(Avg('finalRating')).get('finalRating__avg')


    context_dict['eateries'] = eatery_list

    # Render the response and send it back!
    return render(request, 'gugrub/index.html', context_dict)


def eatery(request, eatery_name_slug):

    context_dict = {}

    try:
        eatery = Eatery.objects.get(slug=eatery_name_slug)

        reviews = Review.objects.filter(eatery=eatery)

        eatery.averageQualityRating = reviews.aggregate(Avg('qualityRating')).get('qualityRating__avg', 0.00)
        eatery.averageValueRating = reviews.aggregate(Avg('valueRating')).get('valueRating__avg', 0.00)
        eatery.averageAtmosphereRating = reviews.aggregate(Avg('atmosphereRating')).get('atmosphereRating__avg', 0.00)
        eatery.averageServiceRating = reviews.aggregate(Avg('serviceRating')).get('serviceRating__avg', 0.00)
        eatery.averageRecommendRating = reviews.aggregate(Avg('recommendRating')).get('recommendRating__avg', 0.00)

        context_dict['reviews'] = reviews

        context_dict['eatery'] = eatery


    except Eatery.DoesNotExist:

        pass

    return render(request, 'gugrub/eatery.html', context_dict)

@login_required
def add_eatery_review(request, eatery_name_slug):

    try:
        eatery = Eatery.objects.get(slug=eatery_name_slug)
    except Eatery.DoesNotExist:
        eatery = None

    if request.method == 'POST':
        form = EateryReviewForm(request.POST, request.FILES, user=request.user)


        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.eatery = eatery
            new_review.reviewer = request.user
            new_review.save()

            return index(request)
        else:

            print form.errors
    else:

        form = EateryReviewForm()

    return render(request, 'gugrub/add_eatery_review.html', {'form': form, 'eatery_name': eatery.name, 'eatery_slug': eatery_name_slug})

@login_required
def add_new_review(request):

    if request.method == 'POST':
        form = NewReviewForm(request.POST, request.FILES, user=request.user)

        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.reviewer = request.user
            new_review.save()

            return index(request)
        else:

            print form.errors
    else:

        form = NewReviewForm()

    return render(request, 'gugrub/add_new_review.html', {'form': form})

