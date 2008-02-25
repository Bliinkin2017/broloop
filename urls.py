from django.conf.urls.defaults import *
from django.conf import settings
from wedding.views import news

urlpatterns = patterns('',
    (r'^news/$', news),
    # Example:
    # (r'^wedding/', include('wedding.foo.urls')),

    # Uncomment this for admin:
#     (r'^admin/', include('django.contrib.admin.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/aaron/projects/wedding/static'}),
    )
