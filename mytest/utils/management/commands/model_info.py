from django.core.management.base import NoArgsCommand
from django.db.models import get_models


class Command(NoArgsCommand):

    help = 'Prints project model names and object count.'
    #requires_model_validation = True

    def handle_noargs(self, **options):
        for model in get_models():
            n = "[%s] - %d  objects\n" % (model.__name__, model.objects.count())
            self.stdout.write(n)
            self.stderr.write("Error: %s" % n)
