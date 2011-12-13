from django.shortcuts import get_object_or_404
from django.views.generic.simple import direct_to_template
from mytest.persons.models import Person, RequestInfo
from mytest.persons.forms import PersonForm


def person_detail(request, person_id=1):

    """ Display person information """

    instance = get_object_or_404(Person, pk=person_id)
    form = PersonForm(instance=instance)
    return direct_to_template(request, 'persons/person_detail.html', {'form': form})


def request_list(request):

    """ Display the first ten request in bd """

    requests = RequestInfo.objects.all().order_by('time')[:10]
    #print request.META
    return direct_to_template(request, 'persons/request_list.html', {'requests': requests})
