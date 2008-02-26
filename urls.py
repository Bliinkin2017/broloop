from django.conf.urls.defaults import *
from django.conf import settings
from wedding.views import news, hotels, registration, info, comments

urlpatterns = patterns('',
    (r'^/$', news),
    (r'^news/$', news),
    (r'^hotels/$', hotels),
    (r'^registration/$', registration),
    (r'^info/$', info),
    (r'^comments/$', comments),
    (r'^admin/', include('django.contrib.admin.urls')),
    # Example:
    # (r'^wedding/', include('wedding.foo.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/aaron/projects/django-site/static'}),
    )
