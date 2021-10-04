from django.conf.urls import url 
from FormacionIntegral import views 
 
from django.urls import include, path
from .views import registroInCreate, registroInList, registroInDetail, registroInUpdate, registroInDelete

urlpatterns = [
    path('create/', registroInCreate.as_view(), name='crear-Registro'),
    path('', registroInList.as_view()),
    path('<int:pk>/', registroInDetail.as_view(), name='retrieve-Registro'),
    path('update/<int:pk>/', registroInUpdate.as_view(), name='actualizar-Registro'),
    path('delete/<int:pk>/', registroInDelete.as_view(), name='eliminar-Registro')
]