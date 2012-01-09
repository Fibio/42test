from django.contrib import admin
from mytest.persons.models import Person, RequestInfo, ModelEntry


def increase(modeladmin, request, queryset):
    queryset.update(_priority=1)
increase.short_description = "Increase priority of selected requests"


def decrease(modeladmin, request, queryset):
    queryset.update(_priority=0)
decrease.short_description = "Decrease priority of selected requests"


class PersonAdmin(admin.ModelAdmin):
    pass


class RequestInfoAdmin(admin.ModelAdmin):
    list_display = ('time', 'request_method', 'user', 'server_protocol', 'priority')
    ordering = ('time',)
    actions = [increase, decrease]


class ModelEntryAdmin(admin.ModelAdmin):
    ordering = ('action_time',)


admin.site.register(Person, PersonAdmin)
admin.site.register(RequestInfo, RequestInfoAdmin)
admin.site.register(ModelEntry, ModelEntryAdmin)
