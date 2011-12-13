from django.conf import settings


def project_settings(request):

    """ Adding project setting in context """

    return {"settings": settings}
