from django.conf.urls import url 
from Alumnos import views 
 
from django.urls import include, path
from .views import AlumnosCreate, AlumnosList, AlumnosDetail, AlumnosUpdate, AlumnosDelete

urlpatterns = [
    path('create/', AlumnosCreate.as_view(), name='crear-evento'),
    path('', AlumnosList.as_view()),
    path('<int:pk>/', AlumnosDetail.as_view(), name='retrieve-evento'),
    path('update/<int:pk>/', AlumnosUpdate.as_view(), name='actualizar-evento'),
    path('delete/<int:pk>/', AlumnosDelete.as_view(), name='eliminar-evento')
]