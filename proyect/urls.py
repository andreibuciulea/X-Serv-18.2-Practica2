from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'acorta.views.form'),	
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(.*)$', 'acorta.views.acortar'),
)

