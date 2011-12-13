from mytest.persons.models import RequestInfo


class RequestInfoLog():
    """ Keep RequestInfo in db """
    def process_request(self, request):
        inst = RequestInfo()
        for field in inst.__dict__.keys():
            if not field.startswith('_') and field != 'id' and field != 'time':
                setattr(inst, field, request.META.get(field.upper(), ''))
        inst.save()