from django.contrib import admin
from .models import eventos

# Register your models here.
@admin.register(eventos)
class eventosAdmin(admin.ModelAdmin):
    list_display = ('pk', 'tituloEvento', 'unidadResponsable', 'fechaEvento', 'cupo', 'creditos')
    list_editable = ('tituloEvento', 'unidadResponsable', 'fechaEvento', 'cupo', 'creditos')
    """ list_filter = ('fechaEvento') """