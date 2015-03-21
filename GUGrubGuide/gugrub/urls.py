from django.conf.urls import patterns, url
from gugrub import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^eatery/(?P<eatery_name_slug>[\w\-]+)/$', views.eatery, name='eatery'),
        url(r'^eatery/(?P<eatery_name_slug>[\w\-]+)/add_eatery_review/$', views.add_eatery_review, name='add_eatery_review'),
        url(r'^add_new_review/$', views.add_new_review, name='add_new_review'),
        )
