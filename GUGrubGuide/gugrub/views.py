from django.http import HttpResponse
from django.shortcuts import render
from gugrub.models import Eatery, Review
from gugrub.forms import ReviewForm

def index(request):
    eatery_list = Eatery.objects.order_by('name')[:5]
    context_dict = {'eateries': eatery_list}

    # Render the response and send it back!
    return render(request, 'gugrub/index.html', context_dict)


def eatery(request, eatery_name_slug):

    context_dict = {}

    try:
        eatery = Eatery.objects.get(slug=eatery_name_slug)
        context_dict['eatery_name'] = eatery.name

        reviews = Review.objects.filter(eatery=eatery)

        context_dict['reviews'] = reviews

        context_dict['eatery'] = eatery
    except Eatery.DoesNotExist:

        pass

    return render(request, 'gugrub/eatery.html', context_dict)

def add_review(request):

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)


        if form.is_valid():
            review_pic = Review(picture= request.FILES['picture'])
            review_pic.save()

            form.save(commit=True)


            return index(request)
        else:

            print form.errors
    else:

        form = ReviewForm()

    return render(request, 'gugrub/add_review.html', {'form': form})