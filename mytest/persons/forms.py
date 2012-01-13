from django import forms
from mytest.persons.models import Person
import django_tables as tables
from django.utils.safestring import mark_safe
from django.utils.html import escape
from django.conf import settings


class ImageViewWidget(forms.widgets.FileInput):
    """
    Widget for image preview
    if edit is True image can be edited
    img_size contains image width and height for preview
    """
    template_with_initial = u'<a href="%(url)s" target="_blank">%(img)s</a> %(input)s %(clear)s'

    def __init__(self, attrs=None, edit=None, img_size=None):
        super(ImageViewWidget, self).__init__(attrs)
        self.edit = edit
        self.img_size = img_size

    def render(self, name, value, attrs=None):
        subst = {'input': '', 'clear': ''}
        template = u'<span>No image</span> %(input)s'
        if self.edit:
            subst['input'] = super(ImageViewWidget, self).render(name, value, attrs)
        if value and hasattr(value, "url"):
            template = self.template_with_initial
            subst['url'] = escape(value.url)
            attrs.update({'src': value.url})
            if self.img_size:
                attrs.update({'width': self.img_size[0], 'height': self.img_size[1]})
            attrs['id'] = attrs.pop('id', 'id') + '_img'
            subst['img'] = u'<img %s>' % forms.util.flatatt(attrs)
            if not self.is_required and self.edit:
                subst['clear'] = u'<br>Delete %s' % forms.widgets.CheckboxInput().render(name,
                                                                            False, attrs=attrs)
        return mark_safe(template % subst)

    def value_from_datadict(self, data, files, name):
        upload = super(ImageViewWidget, self).value_from_datadict(data, files, name)
        if not self.is_required and forms.widgets.CheckboxInput().value_from_datadict(
            data, files, name):
            if upload:
                return object()
            return False
        return upload


class CalendarWidget(forms.TextInput):

    """ Widget for date imput """

    class Media:
        js = ('/admin/jsi18n/',
                  settings.MEDIA_URL + 'js/calendar/core.js',
                  settings.MEDIA_URL + "js/calendar/calendar.js",
                  settings.MEDIA_URL + "js/calendar/DateTimeShortcuts.js")
        css = {'all': (
                settings.MEDIA_URL + 'css/widgets.css',)}

    def __init__(self, attrs={}):
            super(CalendarWidget, self).__init__(attrs={'class': 'vDateField'})


class PersonForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        edit = kwargs.pop('edit', None)
        img_size = kwargs.pop('img_size', None)
        super(PersonForm, self).__init__(*args, **kwargs)
        self.fields['photo'].widget = ImageViewWidget(edit=edit, img_size=img_size)
        if edit:
            self.fields['birth_date'].widget = CalendarWidget(attrs={
                                                    'class': 'vDateField',
                                                    'size': '100'})

    class Media:
        js = (settings.MEDIA_URL + "js/jquery-1.7.1.min.js",
              settings.MEDIA_URL + "js/jquery.form.js",
              settings.MEDIA_URL + "js/save_form.js"
              )

    class Meta:
        model = Person
        widgets = {
            'bio': forms.widgets.Textarea(attrs={'cols': 45, 'rows': 10}),
            'other_contacts': forms.widgets.Textarea(attrs={'cols': 45, 'rows': 10}),
            }
        labels = {'birth_date': 'Date of birth'}


class RequestTable(tables.MemoryTable):

    check = tables.Column(data='id')
    id = tables.Column()
    user = tables.Column()
    time = tables.Column()
    request_method = tables.Column()
    server_protocol = tables.Column()
    lang = tables.Column()
    priority = tables.Column()
