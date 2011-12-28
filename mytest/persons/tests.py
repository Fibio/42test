from django.test import TestCase
from models import Person, RequestInfo
from django.conf import settings
from django.contrib.auth.models import User
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


class LoginEditTestCase(TestCase):

    def setUp(self):
        self.username = 'SuperPuper'
        self.pw = 'pwpwpw'
        self.user = User.objects.create_user(self.username, '', self.pw)
        self.user.is_staff = True
        self.user.is_superuser = True
        self.user.save()
        self.assertTrue(self.client.login(username=self.username, password=self.pw))
        self.post_data = {'first_name': 'John',
                          'last_name': 'Doe',
                          'birth_date': '2011-11-11',
                          'bio': 'some bio',
                          'email': 'john_doe@gmail.com',
                          'skype': 'john_doe'}

    def test_login_main(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, self.username)

    def test_login_system(self):
        self.client.logout()
        response = self.client.get(reverse('edit'))
        self.assertEqual(response.status_code, 302)
        self.client.login(username=self.username, password=self.pw)
        response = self.client.get(reverse('edit'))
        self.assertEqual(response.status_code, 200)

    def test_change_info(self):
        self.assertTrue(self.client.login(username=self.username, password=self.pw))
        self.client.post(reverse('edit'), self.post_data, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        person = Person.objects.get(pk=1)
        self.assertEqual(person.first_name, 'John')
        self.assertEqual(person.last_name, 'Doe')
        self.assertEqual(person.skype, 'john_doe')

    def test_calendar_widget(self):
        js = 'calendar.js"></script>'
        response = self.client.get(reverse('edit'))
        self.assertContains(response, js, count=1)

    def test_error_views(self):
        self.post_data['birth_date'] = ''
        response = self.client.post(reverse('edit'), self.post_data, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertContains(response, 'Fail', count=1)
        self.assertContains(response, '"birth_date", "This field is required."', count=1)
