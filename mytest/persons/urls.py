from django.contrib.auth.decorators import login_required
from django.conf.urls.defaults import patterns, url
from mytest.persons.views import person_detail, request_list

urlpatterns = patterns('',
    url(r'^$', person_detail, name="home"),
    url(r'^request/$', request_list, name="requests" ),
    url(r'^edit/$', login_required(person_detail), {'edit': True}, name="edit" ),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'persons/login.html'}, name='auth_login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', name='auth_logout'),
    url(r'^admin/jsi18n/', 'django.views.i18n.javascript_catalog')
)
