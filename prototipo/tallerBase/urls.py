from django.urls import path
from . import views
from django.conf.urls import handler404

urlpatterns = [
    path('', views.index, name='index'),
    path('requerimiento/', views.requerimiento, name="requerimientos"),
    path('requerimientoEspecif/', views.requerimientoEspecif, name="requerimientosEspecif"),
    path('cliente/',views.clientes,name="clientes"),
    path('add_cliente/',views.add_cliente,name="add_cliente"),
    path('add_requerimiento/', views.add_requerimiento, name="add_requerimiento"),
    path('add_requerimientoEspecif/',views.add_requerimientoEspecif,name="add_requerimientoEspecif")

]

handler404 = 'tallerBase.views.error_404'