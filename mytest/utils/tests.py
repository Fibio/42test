from django.test import TestCase
from django.template import Template, Context
from django.contrib.auth.models import User, AnonymousUser


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
