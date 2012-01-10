from mytest.persons.models import RequestInfo


class RequestInfoLog():

    """ Keep RequestInfo in db """

    def process_request(self, request):
        inst = RequestInfo()
        for field in inst.__dict__.keys():
            if not field.startswith('_') and field != 'id':
                max_length = inst._meta.get_field(field).max_length
                try:
                    value = request.META.get(field.upper(), inst.serializable_value(field))[:max_length]
                except TypeError:
                    value = request.META.get(field.upper(), inst.serializable_value(field))
                setattr(inst, field, value)
        inst.save()
