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
        eatery.averageRating = reviews.aggregate(Avg('finalRating'))
        eatery.averageQualityRating = reviews.aggregate(Avg('qualityRating'))


    context_dict['eateries'] = eatery_list

    # Render the response and send it back!
    return render(request, 'gugrub/index.html', context_dict)


def eatery(request, eatery_name_slug):

    context_dict = {}

    try:
        eatery = Eatery.objects.get(slug=eatery_name_slug)
        context_dict['eatery_name'] = eatery.name
        context_dict['picture'] = eatery.picture

        reviews = Review.objects.filter(eatery=eatery)

        avgQ = reviews.aggregate(Avg('finalRating'))

        context_dict['reviews'] = reviews

        context_dict['eatery'] = eatery

        context_dict['avgQ'] = avgQ

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

def register(request):

    registered = False

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)

        if user_form.is_valid():

            user = user_form.save()

            user.set_password(user.password)
            user.save()

            registered = True

        else:
            print user_form.errors

    else:
        user_form = UserForm()

    return render(request,
            'gugrub/register.html',
            {'user_form': user_form, 'registered': registered})

def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:

            if user.is_active:

                login(request, user)
                return HttpResponseRedirect('/gugrub/')

            else:
                return HttpResponse("Your GuGrubGuide account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'gugrub/login.html', {})

@login_required
def user_logout(request):
    logout(request)

    return HttpResponseRedirect('/gugrub/')