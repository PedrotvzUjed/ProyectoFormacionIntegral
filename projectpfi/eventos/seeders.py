from django.http import HttpResponse
from django.contrib.auth.models import Group
from Alumnos.models import Alumnos
from eventos.models import *

#Seeder Django
def SeederModel(request):
    #SeederClasificacion(request)
    seederCategorias1(request)
    return HttpResponse('listo')

def SeederClasificacion(request):
    dataClasif = [
        {
            'id'    : 1,
            'text'  : 'Arte'
        },
        {
            'id'    : 2,
            'text'  : 'Ciencia'
        },
        {
            'id'    : 3,
            'text'  : 'Deporte'
        },
        {
            'id'    : 4,
            'text'  : 'Civismo'
        },
        {
            'id'    : 5,
            'text'  : 'Responsabilidad Social Universitaria'
        },
        {
            'id'    : 6,
            'text'  : 'Emprendimiento'
        },
    ]
    for d in dataClasif:
        clasifi_cat.objects.create(id = d['id'], text = d['text'])

def seederCategorias1(request):
    dataCat = [
        {
            'id'    : 1,
            'text'  : 'Vinvulación',
            'clasif_id': 2
        },
        {
            'id'    : 2,
            'text'  : 'Formación',
            'clasif_id': 2
        },
        {
            'id'    : 3,
            'text'  : 'Investigación',
            'clasif_id': 2
        },


        {
            'id'    : 4,
            'text'  : 'Deportes Atléticos',
            'clasif_id': 3
        },
        {
            'id'    : 5,
            'text'  : 'Deportes de Pelota',
            'clasif_id': 3
        },
        {
            'id'    : 6,
            'text'  : 'Deportes de Combate',
            'clasif_id': 3
        },
        {
            'id'    : 7,
            'text'  : 'Deportos de Motor',
            'clasif_id': 3
        },
        {
            'id'    : 8,
            'text'  : 'Deportes de Naturaleza',
            'clasif_id': 3
        },

        {
            'id'    : 9,
            'text'  : 'Normas de Cortesia',
            'clasif_id': 4
        },
        {
            'id'    : 10,
            'text'  : 'Urbanidad',
            'clasif_id': 4
        },
        {
            'id'    : 11,
            'text'  : 'Integridad',
            'clasif_id': 4
        },
        {
            'id'    : 12,
            'text'  : 'Educación',
            'clasif_id': 4
        },
        {
            'id'    : 13,
            'text'  : 'Valores Cívicos',
            'clasif_id': 4
        },

    ]
    for d in dataCat:
        catalogo_categorias.objects.create(id = d['id'], text = d['text'], clasificacion_id = d['clasif_id'])

    dataReg = [
        {
            'id'    : 1,
            'text'  : 'Difusión',
            'catalogo_id': 1
        },
        {
            'id'    : 2,
            'text'  : 'Divulgación',
            'catalogo_id': 1
        },
        {
            'id'    : 3,
            'text'  : 'Comunicación',
            'catalogo_id': 1
        },

        {
            'id'    : 4,
            'text'  : 'Contenidos Curriculares',
            'catalogo_id': 2
        },
        {
            'id'    : 5,
            'text'  : 'Habilidades, Actitudes y Valores',
            'catalogo_id': 2
        },

        {
            'id'    : 6,
            'text'  : 'Aplicada',
            'catalogo_id': 2
        },
        {
            'id'    : 7,
            'text'  : 'Documental',
            'catalogo_id': 2
        },

        {
            'id'    : 8,
            'text'  : 'De Campo',
            'catalogo_id': 2
        },
        {
            'id'    : 9,
            'text'  : 'Experimental',
            'catalogo_id': 2
        },
        {
            'id'    : 10,
            'text'  : 'Exploratoria',
            'catalogo_id': 2
        },
        {
            'id'    : 11,
            'text'  : 'Descriptiva',
            'catalogo_id': 2
        },       

        {
            'id'    : 12,
            'text'  : 'Atletismo',
            'catalogo_id': 1
        },
        {
            'id'    : 13,
            'text'  : 'Gimnasia',
            'catalogo_id': 1
        },
        {
            'id'    : 14,
            'text'  : 'Halterofilia',
            'catalogo_id': 1
        },
        {
            'id'    : 15,
            'text'  : 'Natación',
            'catalogo_id': 1
        },
        {
            'id'    : 16,
            'text'  : 'Ciclismo',
            'catalogo_id': 1
        },

        {
            'id'    : 17,
            'text'  : 'Fútbol',
            'catalogo_id': 2
        },
        {
            'id'    : 18,
            'text'  : 'Béisbol',
            'catalogo_id': 2
        },

        {
            'id'    : 19,
            'text'  : 'Rugby',
            'catalogo_id': 2
        },
        {
            'id'    : 20,
            'text'  : 'Baloncesto',
            'catalogo_id': 2
        },
        {
            'id'    : 21,
            'text'  : 'Balnomano',
            'catalogo_id': 2
        },
        {
            'id'    : 22,
            'text'  : 'Voleibol',
            'catalogo_id': 2
        },
        {
            'id'    : 23,
            'text'  : 'Tenis',
            'catalogo_id': 2
        },

        {
            'id'    : 24,
            'text'  : 'Boxeo',
            'catalogo_id': 3
        },
        {
            'id'    : 25,
            'text'  : 'Lucha Libre',
            'catalogo_id': 3
        },
        {
            'id'    : 26,
            'text'  : 'Esgrima',
            'catalogo_id': 3
        },
        {
            'id'    : 27,
            'text'  : 'Artes Marciales',
            'catalogo_id': 3
        },

        {
            'id'    : 28,
            'text'  : 'Automovilismo',
            'catalogo_id': 4
        },
        {
            'id'    : 29,
            'text'  : 'Motociclismo',
            'catalogo_id': 4
        },
        {
            'id'    : 30,
            'text'  : 'Motocross',
            'catalogo_id': 4
        },

        {
            'id'    : 31,
            'text'  : 'Correr en Entornos Abiertos',
            'catalogo_id': 5
        },
        {
            'id'    : 32,
            'text'  : 'Andar en Bicicleta en Entornos Abiertos',
            'catalogo_id': 5
        },

        {
            'id'    : 33,
            'text'  : 'Puntualidad',
            'catalogo_id': 9
        },
        {
            'id'    : 34,
            'text'  : 'Saludar',
            'catalogo_id': 9
        },
        {
            'id'    : 35,
            'text'  : 'Ser Amable',
            'catalogo_id': 9
        },
        {
            'id'    : 36,
            'text'  : 'Honestidad',
            'catalogo_id': 9
        },
        {
            'id'    : 37,
            'text'  : 'Ser Respetuoso',
            'catalogo_id': 9
        },

        {
            'id'    : 38,
            'text'  : 'Responsabilidad Social',
            'catalogo_id': 10
        },
        {
            'id'    : 39,
            'text'  : 'Cuidado del Entorno',
            'catalogo_id': 10
        },

        {
            'id'    : 40,
            'text'  : 'Rectitud',
            'catalogo_id': 11
        },
        {
            'id'    : 41,
            'text'  : 'Sinceridad',
            'catalogo_id': 11
        },
        {
            'id'    : 42,
            'text'  : 'Libertad',
            'catalogo_id': 11
        },
        {
            'id'    : 43,
            'text'  : 'Honestidad',
            'catalogo_id': 11
        },

        {
            'id'    : 44,
            'text'  : 'Inclusiva',
            'catalogo_id': 12
        },
        {
            'id'    : 45,
            'text'  : 'Equitativa',
            'catalogo_id': 12
        },
        {
            'id'    : 46,
            'text'  : 'De Calidad',
            'catalogo_id': 12
        },
        {
            'id'    : 47,
            'text'  : 'Permanente',
            'catalogo_id': 12
        },

        {
            'id'    : 48,
            'text'  : 'Libertad',
            'catalogo_id': 13
        },
        {
            'id'    : 49,
            'text'  : 'Humildad',
            'catalogo_id': 13
        },
        {
            'id'    : 50,
            'text'  : 'Justicia',
            'catalogo_id': 13
        },
        {
            'id'    : 51,
            'text'  : 'Respeto',
            'catalogo_id': 13
        },
        {
            'id'    : 52,
            'text'  : 'Cooperación',
            'catalogo_id': 13
        },
        {
            'id'    : 53,
            'text'  : 'Igualdad Social',
            'catalogo_id': 13
        },
        {
            'id'    : 54,
            'text'  : 'Responsabilidad Social',
            'catalogo_id': 13
        },
        {
            'id'    : 55,
            'text'  : 'Patriotismo',
            'catalogo_id': 13
        },
        
    ]
    for d in dataReg:
        catalogo_categorias2.objects.create(id = d['id'], text = d['text'], catalogo_id = d['catalogo_id'])

    
def SeederCiencia(request):
    dataCat = [
        {
            'id'    : 1,
            'text'  : 'Vinvulación',
            'clasif_id': 2
        },
        {
            'id'    : 2,
            'text'  : 'Formación',
            'clasif_id': 2
        },
        {
            'id'    : 3,
            'text'  : 'Investigación',
            'clasif_id': 2
        },
    ]
    for d in dataCat:
        catalogo_ciencia.objects.create(id = d['id'], text = d['text'], clasificacion = d['clasif_id'])

    dataReg = [
        {
            'id'    : 1,
            'text'  : 'Difusión',
            'catalogo_id': 1
        },
        {
            'id'    : 2,
            'text'  : 'Divulgación',
            'catalogo_id': 1
        },
        {
            'id'    : 3,
            'text'  : 'Comunicación',
            'catalogo_id': 1
        },

        {
            'id'    : 4,
            'text'  : 'Contenidos Curriculares',
            'catalogo_id': 2
        },
        {
            'id'    : 5,
            'text'  : 'Habilidades, Actitudes y Valores',
            'catalogo_id': 2
        },

        {
            'id'    : 6,
            'text'  : 'Aplicada',
            'catalogo_id': 2
        },
        {
            'id'    : 7,
            'text'  : 'Documental',
            'catalogo_id': 2
        },

        {
            'id'    : 8,
            'text'  : 'De Campo',
            'catalogo_id': 2
        },
        {
            'id'    : 9,
            'text'  : 'Experimental',
            'catalogo_id': 2
        },
        {
            'id'    : 10,
            'text'  : 'Exploratoria',
            'catalogo_id': 2
        },
        {
            'id'    : 11,
            'text'  : 'Descriptiva',
            'catalogo_id': 2
        },       
        
    ]
    for d in dataReg:
        categorias_ciencia.objects.create(id = d['id'], text = d['text'], catalogo_id = d['catalogo_id'])
    
def SeederCivismo(request):
    dataCat = [
        {
            'id'    : 1,
            'text'  : 'Normas de Cortesia',
            'clasif_id': 4
        },
        {
            'id'    : 2,
            'text'  : 'Urbanidad',
            'clasif_id': 4
        },
        {
            'id'    : 3,
            'text'  : 'Integridad',
            'clasif_id': 4
        },
        {
            'id'    : 4,
            'text'  : 'Educación',
            'clasif_id': 4
        },
        {
            'id'    : 5,
            'text'  : 'Valores Cívicos',
            'clasif_id': 4
        },
    ]
    for d in dataCat:
        catalogo_civismo.objects.create(id = d['id'], text = d['text'], clasificacion = d['clasif_id'])

    dataReg = [
        {
            'id'    : 1,
            'text'  : 'Puntualidad',
            'catalogo_id': 1
        },
        {
            'id'    : 2,
            'text'  : 'Saludar',
            'catalogo_id': 1
        },
        {
            'id'    : 3,
            'text'  : 'Ser Amable',
            'catalogo_id': 1
        },
        {
            'id'    : 4,
            'text'  : 'Honestidad',
            'catalogo_id': 1
        },
        {
            'id'    : 5,
            'text'  : 'Ser Respetuoso',
            'catalogo_id': 1
        },

        {
            'id'    : 6,
            'text'  : 'Responsabilidad Social',
            'catalogo_id': 2
        },
        {
            'id'    : 7,
            'text'  : 'Cuidado del Entorno',
            'catalogo_id': 2
        },

        {
            'id'    : 8,
            'text'  : 'Rectitud',
            'catalogo_id': 3
        },
        {
            'id'    : 9,
            'text'  : 'Sinceridad',
            'catalogo_id': 3
        },
        {
            'id'    : 10,
            'text'  : 'Libertad',
            'catalogo_id': 3
        },
        {
            'id'    : 11,
            'text'  : 'Honestidad',
            'catalogo_id': 3
        },

        {
            'id'    : 12,
            'text'  : 'Inclusiva',
            'catalogo_id': 4
        },
        {
            'id'    : 13,
            'text'  : 'Equitativa',
            'catalogo_id': 4
        },
        {
            'id'    : 14,
            'text'  : 'De Calidad',
            'catalogo_id': 4
        },
        {
            'id'    : 15,
            'text'  : 'Permanente',
            'catalogo_id': 4
        },

        {
            'id'    : 16,
            'text'  : 'Libertad',
            'catalogo_id': 5
        },
        {
            'id'    : 17,
            'text'  : 'Humildad',
            'catalogo_id': 5
        },
        {
            'id'    : 18,
            'text'  : 'Justicia',
            'catalogo_id': 5
        },
        {
            'id'    : 19,
            'text'  : 'Respeto',
            'catalogo_id': 5
        },
        {
            'id'    : 20,
            'text'  : 'Cooperación',
            'catalogo_id': 5
        },
        {
            'id'    : 21,
            'text'  : 'Igualdad Social',
            'catalogo_id': 5
        },
        {
            'id'    : 22,
            'text'  : 'Responsabilidad Social',
            'catalogo_id': 5
        },
        {
            'id'    : 23,
            'text'  : 'Patriotismo',
            'catalogo_id': 5
        },
        
    ]
    for d in dataReg:
        catalogo_registro_civismo.objects.create(id = d['id'], text = d['text'], catalogo_id = d['catalogo_id'])

