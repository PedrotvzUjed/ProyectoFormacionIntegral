from django.http import HttpResponse
from django.contrib.auth.models import Group
from Alumnos.models import Alumnos
from eventos.models import *

#Seeder Django
def SeederModel(request):
    #SeederClasificacion(request)
    seederCategorias(request)
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

def seederCategorias(request):
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

        {
            'id'    : 14,
            'text'  : 'Artes Visuales',
            'clasif_id': 1
        },
        {
            'id'    : 15,
            'text'  : 'Artes Auditivas',
            'clasif_id': 1
        },
        {
            'id'    : 16,
            'text'  : 'Artes Escenicas y Audiovisuales',
            'clasif_id': 1
        },
        {
            'id'    : 17,
            'text'  : 'Artes Literarias',
            'clasif_id': 1
        },
        {
            'id'    : 18,
            'text'  : 'Filosofía',
            'clasif_id': 1
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
            'catalogo_id': 3
        },
        {
            'id'    : 7,
            'text'  : 'Documental',
            'catalogo_id': 3
        },

        {
            'id'    : 8,
            'text'  : 'De Campo',
            'catalogo_id': 3
        },
        {
            'id'    : 9,
            'text'  : 'Experimental',
            'catalogo_id': 3
        },
        {
            'id'    : 10,
            'text'  : 'Exploratoria',
            'catalogo_id': 3
        },
        {
            'id'    : 11,
            'text'  : 'Descriptiva',
            'catalogo_id': 3
        },       

        {
            'id'    : 12,
            'text'  : 'Atletismo',
            'catalogo_id': 4
        },
        {
            'id'    : 13,
            'text'  : 'Gimnasia',
            'catalogo_id': 4
        },
        {
            'id'    : 14,
            'text'  : 'Halterofilia',
            'catalogo_id': 4
        },
        {
            'id'    : 15,
            'text'  : 'Natación',
            'catalogo_id': 4
        },
        {
            'id'    : 16,
            'text'  : 'Ciclismo',
            'catalogo_id': 4
        },


        {
            'id'    : 17,
            'text'  : 'Fútbol',
            'catalogo_id': 5
        },
        {
            'id'    : 18,
            'text'  : 'Béisbol',
            'catalogo_id': 5
        },
        {
            'id'    : 19,
            'text'  : 'Rugby',
            'catalogo_id': 5
        },
        {
            'id'    : 20,
            'text'  : 'Baloncesto',
            'catalogo_id': 5
        },
        {
            'id'    : 21,
            'text'  : 'Balnomano',
            'catalogo_id': 5
        },
        {
            'id'    : 22,
            'text'  : 'Voleibol',
            'catalogo_id': 5
        },
        {
            'id'    : 23,
            'text'  : 'Tenis',
            'catalogo_id': 5
        },


        {
            'id'    : 24,
            'text'  : 'Boxeo',
            'catalogo_id': 6
        },
        {
            'id'    : 25,
            'text'  : 'Lucha Libre',
            'catalogo_id': 6
        },
        {
            'id'    : 26,
            'text'  : 'Esgrima',
            'catalogo_id': 6
        },
        {
            'id'    : 27,
            'text'  : 'Artes Marciales',
            'catalogo_id': 6
        },


        {
            'id'    : 28,
            'text'  : 'Automovilismo',
            'catalogo_id': 7
        },
        {
            'id'    : 29,
            'text'  : 'Motociclismo',
            'catalogo_id': 7
        },
        {
            'id'    : 30,
            'text'  : 'Motocross',
            'catalogo_id': 7
        },


        {
            'id'    : 31,
            'text'  : 'Correr en Entornos Abiertos',
            'catalogo_id': 8
        },
        {
            'id'    : 32,
            'text'  : 'Andar en Bicicleta en Entornos Abiertos',
            'catalogo_id': 8
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
        
        
        {
            'id'    : 56,
            'text'  : 'Artes Plasticas',
            'catalogo_id': 14
        },
        {
            'id'    : 57,
            'text'  : 'Artes Gráficas',
            'catalogo_id': 14
        },


        {
            'id'    : 58,
            'text'  : 'Música Popular',
            'catalogo_id': 15
        },
        {
            'id'    : 59,
            'text'  : 'Música de Concierto Instrumental',
            'catalogo_id': 15
        },
        {
            'id'    : 60,
            'text'  : 'Música Concierto Vocal',
            'catalogo_id': 15
        },


        {
            'id'    : 61,
            'text'  : 'Teatro',
            'catalogo_id': 16
        },
        {
            'id'    : 62,
            'text'  : 'Danza',
            'catalogo_id': 16
        },
        {
            'id'    : 63,
            'text'  : 'Cine',
            'catalogo_id': 16
        },

        {
            'id'    : 64,
            'text'  : 'Poesia',
            'catalogo_id': 17
        },
        {
            'id'    : 65,
            'text'  : 'Narrativa',
            'catalogo_id': 17
        },
        {
            'id'    : 66,
            'text'  : 'Dramaturgia',
            'catalogo_id': 17
        },
        {
            'id'    : 67,
            'text'  : 'Ensayo',
            'catalogo_id': 17
        },
        {
            'id'    : 68,
            'text'  : 'Crítica',
            'catalogo_id': 17
        },
        
        {
            'id'    : 69,
            'text'  : 'Filosofía',
            'catalogo_id': 18
        },
        
    ]
    for d in dataReg:
        catalogo_categorias2.objects.create(id = d['id'], text = d['text'], catalogo_id = d['catalogo_id'])

    dataCatArte = [
        {
            'id'    : 1,
            'text'  : 'Museo',
            'categoria_id': 56
        },
        {
            'id'    : 2,
            'text'  : 'Pntura',
            'categoria_id': 56
        },
        {
            'id'    : 3,
            'text'  : 'Escultura',
            'categoria_id': 56
        },
        {
            'id'    : 4,
            'text'  : 'Grabado',
            'categoria_id': 56
        },
        {
            'id'    : 5,
            'text'  : 'Dibujo',
            'categoria_id': 56
        },
        

        {
            'id'    : 6,
            'text'  : 'Cerámica',
            'categoria_id': 57
        },
        {
            'id'    : 7,
            'text'  : 'Bordado',
            'categoria_id': 57
        },
        {
            'id'    : 8,
            'text'  : 'Cesteria',
            'categoria_id': 57
        },
        {
            'id'    : 9,
            'text'  : 'Repujado',
            'categoria_id': 57
        },
        {
            'id'    : 10,
            'text'  : 'Vitrales',
            'categoria_id': 57
        },
        {
            'id'    : 11,
            'text'  : 'Orfebrería',
            'categoria_id': 57
        },
        

        {
            'id'    : 12,
            'text'  : 'Comercial',
            'categoria_id': 58
        },
        {
            'id'    : 13,
            'text'  : 'Mezcla',
            'categoria_id': 58
        },
        {
            'id'    : 14,
            'text'  : 'Contemporanea',
            'categoria_id': 58
        },
        {
            'id'    : 15,
            'text'  : 'Folklorica',
            'categoria_id': 58
        },
        {
            'id'    : 16,
            'text'  : 'Autóctona',
            'categoria_id': 58
        },
        {
            'id'    : 17,
            'text'  : 'Etnica',
            'categoria_id': 58
        },
        

        {
            'id'    : 18,
            'text'  : 'Orquesta de Cámara',
            'categoria_id': 59
        },
        {
            'id'    : 19,
            'text'  : 'Orquesta Sinfónica',
            'categoria_id': 59
        },
        {
            'id'    : 20,
            'text'  : 'Ensambles',
            'categoria_id': 59
        },
        {
            'id'    : 21,
            'text'  : 'Instrumental',
            'categoria_id': 59
        },
        {
            'id'    : 22,
            'text'  : 'Solista',
            'categoria_id': 59
        },
        {
            'id'    : 23,
            'text'  : 'Grupos',
            'categoria_id': 59
        },
        
        {
            'id'    : 24,
            'text'  : 'Coral',
            'categoria_id': 60
        },
        {
            'id'    : 25,
            'text'  : 'Ópera',
            'categoria_id': 60
        },
        {
            'id'    : 26,
            'text'  : 'Dirección',
            'categoria_id': 60
        },
        {
            'id'    : 27,
            'text'  : 'Composición',
            'categoria_id': 60
        },
        {
            'id'    : 28,
            'text'  : 'Grupos',
            'categoria_id': 60
        },
        {
            'id'    : 29,
            'text'  : 'Solistas',
            'categoria_id': 60
        },
        

        {
            'id'    : 30,
            'text'  : 'Escenografía',
            'categoria_id': 61
        },
        {
            'id'    : 31,
            'text'  : 'Puesta en Escena',
            'categoria_id': 61
        },
        {
            'id'    : 32,
            'text'  : 'Actuación',
            'categoria_id': 61
        },
        {
            'id'    : 33,
            'text'  : 'Dirección Escenica',
            'categoria_id': 61
        },
        {
            'id'    : 34,
            'text'  : 'Adaptación',
            'categoria_id': 61
        },
        {
            'id'    : 35,
            'text'  : 'Literaria',
            'categoria_id': 61
        },
        

        {
            'id'    : 36,
            'text'  : 'Folklorica',
            'categoria_id': 62
        },
        {
            'id'    : 37,
            'text'  : 'Popular',
            'categoria_id': 62
        },
        {
            'id'    : 38,
            'text'  : 'Moderna',
            'categoria_id': 62
        },
        {
            'id'    : 39,
            'text'  : 'Clásica',
            'categoria_id': 62
        },
        {
            'id'    : 40,
            'text'  : 'Comercial',
            'categoria_id': 62
        },
        

        {
            'id'    : 41,
            'text'  : 'Video',
            'categoria_id': 63
        },
        {
            'id'    : 42,
            'text'  : 'Nuevas Tecnologías',
            'categoria_id': 63
        },

        {
            'id'    : 43,
            'text'  : 'Poesia',
            'categoria_id': 64
        },
        {
            'id'    : 44,
            'text'  : 'Narrativa',
            'categoria_id': 65
        },
        {
            'id'    : 45,
            'text'  : 'Dramaturgia',
            'categoria_id': 66
        },
        {
            'id'    : 46,
            'text'  : 'Ensayo',
            'categoria_id': 67
        },
        {
            'id'    : 47,
            'text'  : 'Crítica',
            'categoria_id': 68
        },

        {
            'id'    : 49,
            'text'  : 'Filosofía',
            'categoria_id': 69
        },
    ]

    for d in dataCatArte:
        arte_categorias.objects.create(id = d['id'], text = d['text'], categoria_id = d['categoria_id'])