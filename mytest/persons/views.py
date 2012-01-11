from django.views.generic.simple import direct_to_template
from django.http import HttpResponse, Http404
from django.utils import simplejson
from mytest.utils import resize
from mytest.persons.models import Person, RequestInfo
from mytest.persons.forms import PersonForm


def person_detail(request, edit=False):

    """ Display person information """

    instance = Person.objects.all()[0]
    if not instance:
        raise Http404
    img_size = resize(instance.photo)
    form = PersonForm(request.POST or None, request.FILES or None, instance=instance,
                      edit=edit, img_size=img_size)
    if request.method == 'POST' and request.is_ajax():
        errors = []
        response_text = 'Empty'
        if form.is_valid():
            f = form.save()
            status = 'Ok'
            if 'photo' in form.changed_data:
                response_text = str(PersonForm(instance=f, edit=edit, img_size=resize(f.photo))['photo'])
        else:
            status = 'Fail'
            errors = [(key, unicode(value[0])) for key, value in form.errors.items()]
        res = {'status': status, 'response_text': response_text, 'errors': errors}
        return HttpResponse(simplejson.dumps(res), mimetype='application/javascript')

    return direct_to_template(request, 'persons/person_detail.html', {'form': form, 'edit': edit})


def request_list(request):

    """ Display the first ten request in bd """
    requests = RequestInfo.objects.all().order_by('time')[:10]
    requests_sort = sorted(requests, key=lambda requests: requests.priority, reverse=True)
    return direct_to_template(request, 'persons/request_list.html', {'requests': requests_sort})
