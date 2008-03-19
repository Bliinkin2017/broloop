from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.simple import direct_to_template
from mysite.wedding.views import news, rsvp, hotels, registration, info, comments

urlpatterns = patterns('',
    (r'^$', news),
    (r'^news/$', news),
    (r'^rsvp/$', rsvp),
    (r'^hotels/$', hotels),
    (r'^registration/$', registration),
    (r'^info/$', info),
    (r'^comments/$', comments, {'page': 0}),
    (r'^comments/(?P<page>\d+)/$', comments),
    (r'^rsvped/$', direct_to_template, {'template': 'rsvped.html'}),
    (r'^thanks/$', direct_to_template, {'template': 'thanks.html'}),
    (r'^admin/', include('django.contrib.admin.urls')),
    # Example:
    # (r'^wedding/', include('wedding.foo.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/aaron/www/static'}),
    )
