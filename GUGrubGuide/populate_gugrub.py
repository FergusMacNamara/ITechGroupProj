__author__ = 'Fergus'

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GUGrubGuide.settings')

import django
django.setup()

from gugrub.models import Eatery, Review
from django.contrib.auth.models import User

def populate():
    cafe_picolino = add_eatery(name="Cafe Picolino",
                               loc="Boyd Orr Building [D1]",
                               desc="Freshly made sandwiches, soup, home baking, hot & cold drinks",
                               url="http://www.gla.ac.uk/services/hospitality/eatingoncampus/")

    cafe_picolino2 = add_eatery(name="Cafe Picolino",
                               loc="Boyd Orr Building [D1]",
                               desc="Freshly made sandwiches, soup, home baking, hot & cold drinks",
                               url="http://www.gla.ac.uk/services/hospitality/eatingoncampus/")

    user = add_user(username="fmacn",
                    email="f.macnamara1@hotmail.com",
                    pw="password",
                    fname="Fergus",
                    lname="MacNamara")

    add_review(eatery=cafe_picolino,
                rvr= user,
                title="Boyd Orr Cafe",
                desc="Review text here",
                qualR=4,
                valR=2,
                atmosR=3,
                servR=4,
                recR=3)

def add_eatery(name, loc, desc, url):
    p = Eatery.objects.get_or_create(name=name,
                                     location=loc,
                                     description=desc,
                                     url=url)[0]

    return p

def add_user(username, email, pw, fname, lname):
    u = User.objects.get_or_create(username=username,
                                   email=email,
                                   password=pw,
                                   first_name=fname,
                                   last_name=lname)[0]

    return u

def add_review(eatery, rvr, title, desc, qualR, valR, atmosR, servR, recR):
    r = Review.objects.get_or_create(eatery=eatery,
                                     reviewer=rvr,
                                     title=title,
                                     description=desc,
                                     qualityRating=qualR,
                                     valueRating=valR,
                                     atmosphereRating=atmosR,
                                     serviceRating=servR,
                                     recommendRating=recR)[0]
    return r

# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    populate()
