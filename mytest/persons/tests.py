from django.utils import unittest
from django.test.client import Client
from models import Person


class PersonTestCase(unittest.TestCase):

    """ Test for main page about person information"""

    def setUp(self):
        self.client = Client()
        p = Person()
        p.first_name = 'Jhon'
        p.last_name = 'Doe'
        p.birth_date = '2011-12-09'
        p.skype = 'john_doe'
        p.save()
        self.client = Client()

    def test_person_exists(self):
        person = Person.objects.get(pk=1)
        self.assertIsNotNone(person)

    def test_person_content(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(bool(response.content.find('john_doe')), True)
