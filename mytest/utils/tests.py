from django.test import TestCase
from django.template import Template, Context
from django.contrib.auth.models import User, AnonymousUser
from django.core.management import call_command
from django.db.models import get_models
from StringIO import StringIO
import subprocess
import datetime
import re


class TemplateTagsTestCase(TestCase):

    def setUp(self):
        self.username = 'SuperPuper'
        self.pw = 'pwpwpw'
        self.user = User.objects.create_user(self.username, '', self.pw)
        self.user.is_staff = True
        self.user.is_superuser = True
        self.user.save()
        self.template = Template("{% load custom_tags %}"
                       "{% if user.is_authenticated %}"
                       "{% edit_link user %}"
                       "{% else %}"
                       "{% url auth_login %}"
                       "{% endif %}")#.render(Context({'user': self.user}))
        self.tag_out = u'<br>also you can <a href="/admin/auth/user/1/">edit SuperPuper profile</a>'

    def test_edit_link_auth(self):
        self.assertEqual(self.template.render(Context({'user': self.user})), self.tag_out)

    def test_dit_link_anonim(self):
        self.assertNotEqual(self.template.render(Context({'user': AnonymousUser()})), self.tag_out)


class CommandTestCase(TestCase):

    def setUp(self):
        self.username = 'SuperPuper'
        self.pw = 'pwpwpw'
        self.user = User.objects.create_user(self.username, '', self.pw)
        self.user.is_staff = True
        self.user.is_superuser = True
        self.user.save()
        self.out = StringIO()
        self.err = StringIO()
        self.models = [(model.__name__, str(model.objects.count())) for model in get_models()]
        self.pattern = '.*\[(.*)\] - (\d*).*'

    def __find_match(self, out, pattern):
        out.seek(0)
        out = out.read()
        return re.findall(pattern, out)

    def test_command(self):
        call_command('model_info', stdout=self.out, stderr=self.err)
        self.assertEqual(self.__find_match(self.out, self.pattern), self.models)
        self.assertEqual(self.__find_match(self.err, 'Error' + self.pattern), self.models)

    def test_bash(self):
        subprocess.call('./bashcommand.sh', shell=True, stdout=subprocess.PIPE)
        f = open('%s.dat' % datetime.date.today(), 'r')
        self.assertEqual(self.__find_match(f, 'Error' + self.pattern), self.models)
        subprocess.os.remove('%s.dat' % datetime.date.today())
