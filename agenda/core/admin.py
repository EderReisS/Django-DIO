from django.contrib import admin
from .models import Evento

class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo','data_evento')
    list_filter = ('usuario','data_evento')


# Register your models here.
admin.site.register(Evento,EventoAdmin)