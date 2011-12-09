from django.contrib import admin
from mytest.persons.models import Person


class PersonAdmin(admin.ModelAdmin):
    pass

admin.site.register(Person, PersonAdmin)
