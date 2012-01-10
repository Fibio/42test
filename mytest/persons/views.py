from django.shortcuts import get_object_or_404 #, redirect
from django.views.generic.simple import direct_to_template
from django.http import HttpResponse
from django.utils import simplejson
from PIL import Image
from mytest.persons.models import Person, RequestInfo
from mytest.persons.forms import PersonForm


def resize(img, output_size=(350, 350)):

    """ Return image size for preview """

    if img and hasattr(img, "url"):
        image = Image.open(img)
        m_width = float(output_size[0])
        m_height = float(output_size[1])
        w_k = image.size[0] / m_width
        h_k = image.size[1] / m_height
        if output_size < image.size:
            if w_k > h_k:
                new_size = (m_width, image.size[1] / w_k)
            else:
                new_size = (image.size[0] / h_k, m_height)
        else:
            new_size = image.size
        new_size = tuple(map(int, new_size))
        return new_size
    return None


def person_detail(request, edit=False, person_id=1):

    """ Display person information """

    instance = get_object_or_404(Person, pk=person_id)
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
