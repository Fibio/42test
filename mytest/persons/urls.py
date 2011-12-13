from django.conf.urls.defaults import patterns, url
from mytest.persons.views import person_detail, request_list

urlpatterns = patterns('',
    url(r'^$', person_detail, name="home"),
    url(r'^request/$', request_list, name="requests" ),
)