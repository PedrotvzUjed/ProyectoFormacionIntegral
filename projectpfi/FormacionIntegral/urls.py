from django.conf.urls import url 
from FormacionIntegral import views 
 
from django.urls import include, path
from .views import FormacionInCreate, FormacionInList, FormacionInDetail, FormacionInUpdate, FormacionInDelete, FormacionInEventosList

urlpatterns = [
    path('create/', FormacionInCreate.as_view(), name='crear-Registro'),
    path('', FormacionInList.as_view()),
    path('listEventsData/', FormacionInEventosList.as_view()),
    path('<int:pk>/', FormacionInDetail.as_view(), name='retrieve-Registro'),
    path('update/<int:pk>/', FormacionInUpdate.as_view(), name='actualizar-Registro'),
    #path('put/<int:pk>/', FormacionInUpdate.as_view(), name='actualizar-Registro'),
    path('delete/<int:pk>/', FormacionInDelete.as_view(), name='eliminar-Registro')
]