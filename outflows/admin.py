from django.contrib import admin
from . import models


class OutflowAdmin(admin.ModelAdmin):
    list_display = ('product', 'description',)
    search_fields = ('name',)

admin.site.register(models.Outflow, OutflowAdmin)
