from django import template
from django.core.urlresolvers import reverse


register = template.Library()


class BuildLinkNode(template.Node):

    def __init__(self, obj_str):
        self.object = template.Variable(obj_str)

    def render(self, context):
        try:
            obj = self.object.resolve(context)
            url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.module_name), args=(obj.pk,))
            return u'<br>also you can <a href="%s">edit %s profile</a>' % (url, obj.__unicode__())
        except:
            return ''


@register.tag
def edit_link(parser, token):
    try:
        tag_name, obj_str = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires exactly one argument" % token.contents.split()[0]
    return BuildLinkNode(obj_str)
