from django.contrib import admin
from mytest.persons.models import Person, RequestInfo, ModelEntry


class PersonAdmin(admin.ModelAdmin):
    pass


class RequestInfoAdmin(admin.ModelAdmin):
    list_display = ('time', 'request_method', 'user', 'server_protocol')
    ordering = ('time',)


class ModelEntryAdmin(admin.ModelAdmin):
    ordering = ('action_time',)


admin.site.register(Person, PersonAdmin)
admin.site.register(RequestInfo, RequestInfoAdmin)
admin.site.register(ModelEntry, ModelEntryAdmin)
