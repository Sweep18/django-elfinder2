# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^elfinder/', include('elfinder.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   ]
