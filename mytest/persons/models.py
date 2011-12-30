from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save, post_delete


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    photo = models.ImageField(upload_to="person_images/", blank=True)
    mail = models.EmailField(blank=True)
    jabber = models.EmailField(blank=True)
    skype = models.CharField(max_length=20, blank=True )
    other_contacts = models.TextField(blank=True)
    bio = models.TextField(blank=True)

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


EVENT_CHOICES = {
    True: 'created',
    False: 'edited',
    None: 'deleted'}


MODEL_IGNORE = ['ModelEntry', 'Requestinfo', 'Message', 'Session',
                'LogEntry', 'Permission', 'ContentType', 'Site']


class ModelEntry(models.Model):
    action_time = models.DateTimeField(auto_now=True)
    event = models.CharField(max_length=6)
    content_type = models.ForeignKey(ContentType, blank=True, null=True)
    model_cls = models.CharField(max_length=255)
    object_id = models.IntegerField()

    def __unicode__(self):
        return u'%s instance was %s at %s' % (self.model_cls, self.event, self.action_time)

    class Meta:
        db_table = 'model_entry'
        verbose_name_plural = 'model_entries'


def event(sender, instance, **kwargs):
    if sender.__name__ not in MODEL_IGNORE:
        ModelEntry.objects.create(event=EVENT_CHOICES[kwargs.get('created')],
                                  content_type=ContentType.objects.get_for_model(sender),
                                  model_cls=sender.__name__,
                                  object_id=instance.id)


post_save.connect(event)
post_delete.connect(event)
