from django.conf.urls import patterns, url
from gugrub import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^add_review/$', views.add_review, name='add_review'),
        url(r'^eatery/(?P<eatery_name_slug>[\w\-]+)/$', views.eatery, name='eatery'),)
