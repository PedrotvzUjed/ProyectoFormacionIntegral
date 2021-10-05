from django.contrib import admin
from .models import FormacionIntegral

# Register your models here.
@admin.register(FormacionIntegral)
class FormacionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'nombre', 'matricula', 'asistencia', 'evento', 'alumno')
    list_editable = ('nombre', 'matricula', 'asistencia', 'evento', 'alumno')
    list_filter = ('created', 'modified')