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

    cafe_forthought = add_eatery(name="Food for thought",
                               loc="The Fraser Building, level 3[E2]",
                               desc="For students, staff and visitors to the campus: hot meals and snacks",
                               url="http://www.gla.ac.uk/services/hospitality/eatingoncampus/")

    cafe_togo = add_eatery(name="Food to go",
                               loc="The Fraser Building, level 3[E2]",
                               desc="'Food to go' offers everything you need",
                               url="http://www.gla.ac.uk/services/hospitality/eatingoncampus/")

    cafe_thesquare = add_eatery(name="One A The Square",
                               loc="The Fraser Building, level 3[E2]",
                               desc="For students, staff and visitors to the campus: hot meals and snacks",
                               url="http://www.gla.ac.uk/services/hospitality/eatingoncampus/")

    cafe_atrium = add_eatery(name="Atrium Cafe",
                               loc="Wolfson Medical School Building[C8]",
                               desc="Freshly made sandwiches, baked potatoes, baguettes, soup, home baking, confectionery, hot & cold drinks",
                               url="http://www.gla.ac.uk/services/hospitality/eatingoncampus/")

    cafe_standrews = add_eatery(name="St Andrews Building Cafe",
                               loc="STAC [E14]",
                               desc="Breakfast rolls, freshly made sandwiches, baked potatoes, soup, home baking, confectionary, hot & cold drinks",
                               url="http://www.gla.ac.uk/services/hospitality/eatingoncampus/")

    cafe_links = add_eatery(name="Links Cafe",
                               loc="off the Courtyard, Wolfson Building[B10]",
                               desc="For students, staff and visitors to the campus: hot meals and snacks",
                               url="http://www.gla.ac.uk/services/hospitality/eatingoncampus/")

    garscube_campus = add_eatery(name="Food farm",
                               loc="School of Veterinary Medicine",
                               desc="Breakfast, brasserie-style lunch offer, baked potatoes, baguettes, soup, sandwiches, hot & cold drinks",
                               url="http://www.gla.ac.uk/services/hospitality/eatingoncampus/")

    cafe_focus = add_eatery(name="Food in focus",
                               loc="Level 3, University Library [D11]",
                               desc="For students, staff and visitors to the campus: hot meals and snacks",
                               url="http://www.gla.ac.uk/services/hospitality/eatingoncampus/")

    cafe_postgrad = add_eatery(name="Gilchrist Postgraduate Club",
                               loc="Gilbert Scott Building [A26]",
                               desc="For postgraduate students and staff. University ID/Registration card required for swipe entry system Monday to Friday",
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

    add_review(eatery=cafe_postgrad,
                rvr= user,
                title="Gilbert Scott Building [A26]",
                desc="Review text here",
                qualR=4,
                valR=2,
                atmosR=3,
                servR=4,
                recR=3)

    add_review(eatery=cafe_forthought,
                rvr= user,
                title="The Fraser Building, level 3[E2]",
                desc="Review text here",
                qualR=4,
                valR=2,
                atmosR=3,
                servR=4,
                recR=3)

    add_review(eatery=cafe_togo,
                rvr= user,
                title="The Fraser Building, level 3[E2]",
                desc="Review text here",
                qualR=4,
                valR=2,
                atmosR=3,
                servR=4,
                recR=3)

    add_review(eatery=cafe_thesquare,
                rvr= user,
                title="The Fraser Building, level 3[E2]",
                desc="Review text here",
                qualR=4,
                valR=2,
                atmosR=3,
                servR=4,
                recR=3)

    add_review(eatery=cafe_atrium,
                rvr= user,
                title="Wolfson Medical School Building[C8]",
                desc="Review text here",
                qualR=4,
                valR=2,
                atmosR=3,
                servR=4,
                recR=3)

    add_review(eatery=cafe_standrews,
                rvr= user,
                title="STAC [E14]",
                desc="Review text here",
                qualR=4,
                valR=2,
                atmosR=3,
                servR=4,
                recR=3)

    add_review(eatery=cafe_links,
                rvr= user,
                title="off the Courtyard, Wolfson Building[B10]",
                desc="Review text here",
                qualR=4,
                valR=2,
                atmosR=3,
                servR=4,
                recR=3)

    add_review(eatery=garscube_campus,
                rvr= user,
                title="School of Veterinary Medicine",
                desc="Review text here",
                qualR=4,
                valR=2,
                atmosR=3,
                servR=4,
                recR=3)

    add_review(eatery=cafe_focus,
                rvr= user,
                title="Level 3, University Library [D11]",
                desc="Review here",
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
