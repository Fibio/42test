from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from mytest.persons.models import Person
from mytest.persons.forms import PersonForm


def person_detail(request, person_id=1):

    """ Display person information """

    instance = get_object_or_404(Person, pk=person_id)
    form = PersonForm(instance=instance)
    return render_to_response('persons/person_detail.html', {'form': form})
