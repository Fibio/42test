from django.test import TestCase
from models import Person, RequestInfo
from django.conf import settings
from django.core.urlresolvers import reverse


class PersonTestCase(TestCase):

    """ Test for main page about person information"""

    def test_person_exists(self):
        person = Person.objects.get(pk=1)
        self.assertIsNotNone(person)

    def test_main_content(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, str(Person.objects.get(pk=1).first_name))


class ProcessorsTestCase(TestCase):

    """ Test for main page """

    def test_main_content(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, str(settings.ROOT_URLCONF))
    
    def test_all_settings(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.context['settings'], settings)


class RequestInfoTestCase(TestCase):

    """ Test for middleware about request info"""

    def test_request_content(self):
        response = self.client.get(reverse('requests'))
        self.assertEqual(response.status_code, 200)
        for i in range(15):
            response = self.client.get(reverse('requests'))
        requests = RequestInfo.objects.all().order_by('time')[:10]
        self.assertEqual(list(response.context['requests']), list(requests))
