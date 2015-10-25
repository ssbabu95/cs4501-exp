from django.conf.urls import patterns, include, url
from django.contrib import admin
from cs4501 import main

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cs4501.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home$', main.homepage),
    url(r'^listing/(\d+)$', main.listing_det),
    url(r'^login$', main.login),
    url(r'^logout$', main.logout),
    url(r'^createuser$', main.create_usr),
    url(r'^createlisting$', main.create_lst),
)
