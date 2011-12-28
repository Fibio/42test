from django.conf import settings


def project_settings(request):

    """ Adding project setting in context """

    return {"settings": settings}


def this_url_cp(request):

    """Adding selfurl in context """

    return {'this_url': request.path}
