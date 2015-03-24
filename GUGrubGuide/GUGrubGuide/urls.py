from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from registration.backends.default.views import RegistrationView

# Create a new class that redirects the user to the index page, if successful at logging
class MyRegistrationView(RegistrationView):
    def get_success_url(self,request, user):
        return '/gugrub/'


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^gugrub/', include('gugrub.urls')),
        #Add in this url pattern to override the default pattern in accounts.
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    (r'^accounts/', include('registration.backends.default.urls')),
)
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )