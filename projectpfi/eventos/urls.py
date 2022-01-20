from django.conf.urls import url 
from eventos import views 
 
from django.urls import include, path
from .views import eventosCreate, eventosList, eventosDetail, eventosUpdate, eventosDelete, calendarioCreate, calendarioList, evidencias, evidenciasList, evidenciasUpdate


#urlpatterns = [ 
#  url(r'^api/eventos$', views.eventos_list),
 #   url(r'^api/eventos/(?P<pk>[0-9]+)$', views.eventos_detail)
    #url(r'^api/eventos/published$', views.eventos_list_fechaEvento)
#]

urlpatterns = [
    path('create/', eventosCreate.as_view(), name='crear-evento'),
    path('create/calendario/', calendarioCreate.as_view(), name='crear-calendario'),
    path('', eventosList.as_view()),
    path('calendario', calendarioList.as_view()),
    path('<int:pk>/', eventosDetail.as_view(), name='retrieve-evento'),
    path('update/<int:pk>/', eventosUpdate.as_view(), name='actualizar-evento'),
    #path('put/<int:pk>/', eventosUpdate.as_view(), name='actualizar-evento'),
    path('delete/<int:pk>/', eventosDelete.as_view(), name='eliminar-evento'),
    path('create/evidencia', evidencias.as_view(), name='crear-evidencia'),
    path('update/evidencia/<int:pk>/', evidenciasUpdate.as_view(), name='actualizar-evidencia'),
    path('evidencia',evidenciasList.as_view(), name='retrieve-evidencia')
]
