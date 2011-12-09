from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from mytest.persons.views import person_detail
from django.contrib import admin
admin.autodiscover()

media = {'document_root': settings.MEDIA_ROOT}

urlpatterns = patterns('',
    url(r'^$', person_detail, name='home'),
    # url(r'^mytest/', include('mytest.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
    (r'^media/(?P<path>.*)$', 'serve', media),
    (r'^css/(?P<path>.*)$', 'serve', media),
    (r'^js/(?P<path>.*)$', 'serve', media),
    (r'^img/(?P<path>.*)$', 'serve', media),
    (r'^admin/css/(?P<path>.*)$', 'serve', media),
    (r'^admin/js/(?P<path>.*)$', 'serve', media),
    (r'^admin/img/(?P<path>.*)$', 'serve', media),
    )
