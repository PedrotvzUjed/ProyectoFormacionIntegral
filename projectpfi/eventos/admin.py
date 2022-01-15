from django.contrib import admin
from .models import eventos, eventosCalendario, eventosSubirevidenciasAlumno

# Register your models here.
@admin.register(eventos)
class eventosAdmin(admin.ModelAdmin):
    list_display = ('pk', 'tituloEvento', 'unidadResponsable', 'fechaEvento', 'cupo', 'creditos')
    list_editable = ('tituloEvento', 'unidadResponsable', 'fechaEvento', 'cupo', 'creditos')
    """ list_filter = ('fechaEvento') """

@admin.register(eventosCalendario)
class calendarioAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'start', 'end')
    list_editable = ('name', 'start', 'end')

@admin.register(eventosSubirevidenciasAlumno)
class evidenciasAlumno(admin.ModelAdmin):
    list_display = ('pk','img', 'evento', 'alumno')
    list_editable = ('img', 'evento', 'alumno')