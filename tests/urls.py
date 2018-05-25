from __future__ import unicode_literals

import django

from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = [
    url(
        r'^calendar/', include('happenings.urls', namespace='calendar')
    ),
]

if django.__version__.split('.')[:2] >= ['1', '9']:
    urlpatterns += [
        url(
            r'^admin/', include(admin.site.urls[:2])
        ),
    ]
else:
    urlpatterns += [
        url(
            r'^admin/', include(admin.site.urls)
        ),
    ]

urlpatterns += staticfiles_urlpatterns()
