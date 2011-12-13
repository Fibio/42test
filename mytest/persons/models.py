from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    bio = models.TextField(blank=True)
    mail = models.EmailField(blank=True)
    jabber = models.EmailField(blank=True)
    skype = models.CharField(max_length=20, blank=True )
    other_contacts = models.TextField(blank=True)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    class Meta:
        db_table = 'person'


class RequestInfo(models.Model):
    user = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now=True)
    request_method = models.CharField(max_length=10)
    server_protocol = models.CharField(max_length=10)
    http_connection = models.CharField(max_length=20)
    http_user_agent = models.CharField(max_length=50)
    lang = models.CharField(max_length=20)
    http_accept_charset = models.CharField(max_length=50)
    http_cookie = models.CharField(max_length=100)

    def __unicode__(self):
        return u'Request from %s method - %s, at %s' % (self.user, self.request_method, self.time)

    class Meta:
        db_table = 'request_info'
        verbose_name_plural = 'request_information'
