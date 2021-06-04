from django.contrib import admin
from .models import Contest,Event
# Register your models here.

admin.site.register(Contest)
admin.site.register(Event)

from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

admin.site.site_header = 'Vel tech IP'

AdminSite.site_title = 'IP project'
