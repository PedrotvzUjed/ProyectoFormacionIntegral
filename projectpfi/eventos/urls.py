from django.conf.urls import url 
from eventos import views 
 
from django.urls import include, path
from .views import eventosCreate, eventosList, eventosDetail, eventosUpdate, eventosDelete


#urlpatterns = [ 
#  url(r'^api/eventos$', views.eventos_list),
 #   url(r'^api/eventos/(?P<pk>[0-9]+)$', views.eventos_detail)
    #url(r'^api/eventos/published$', views.eventos_list_fechaEvento)
#]

urlpatterns = [
    path('create/', eventosCreate.as_view(), name='crear-evento'),
    path('', eventosList.as_view()),
    path('<int:pk>/', eventosDetail.as_view(), name='retrieve-evento'),
    path('update/<int:pk>/', eventosUpdate.as_view(), name='actualizar-evento'),
    #path('put/<int:pk>/', eventosUpdate.as_view(), name='actualizar-evento'),
     path('delete/<int:pk>/', eventosDelete.as_view(), name='eliminar-evento')
]
