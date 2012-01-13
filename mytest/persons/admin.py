from django.contrib import admin
from mytest.persons.models import Person, RequestInfo, ModelEntry
from django.db.models import F


def change_priority(queryset, inc=1):
    queryset.update(priority=F('priority') + inc)


def increase(modeladmin, request, queryset):
    change_priority(queryset)

increase.short_description = "Increase priority of selected requests"


def decrease(modeladmin, request, queryset):
    change_priority(queryset, inc=-1)

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
