#from django.utils import unittest
from django.test import TestCase
from django.test.client import Client
from models import Person, RequestInfo
from django.conf import settings


class PersonTestCase(TestCase):

    """ Test for main page about person information"""

    def setUp(self):
        self.client = Client()
        p = Person()
        p.first_name = 'Jhon'
        p.last_name = 'Doe'
        p.birth_date = '2011-12-09'
        p.skype = 'john_doe'
        p.save()

    def test_person_exists(self):
        person = Person.objects.get(pk=1)
        self.assertIsNotNone(person)

    def test_main_content(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'john_doe')


class MainTestCase(PersonTestCase):

    """ Test for main page """

    def test_main_content(self):
        response = self.client.get('/')
        self.assertContains(response, str(settings.ROOT_URLCONF))


class RequestInfoTestCase(TestCase):

    """ Test for middleware about request info"""

    def setUp(self):
        self.client = Client()

    def test_request_content(self):
        response = self.client.get('/request/')
        self.assertEqual(response.status_code, 200)
        for i in range(15):
            response = self.client.get('/request/')
        requests = RequestInfo.objects.all().order_by('time')[:10]
        self.assertEqual(list(response.context['requests']), list(requests))
