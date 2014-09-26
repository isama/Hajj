from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^site/admin', include(admin.site.urls)),
    url(r'^hajj/', include('Web.urls')),
)
