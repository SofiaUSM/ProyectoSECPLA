from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name="menu" ),
    path('create', views.formulario, name="create" ),
    path('actualizar/<int:id>/', views.actualizar, name="actualizar" ),
    path('actualizar_terreno/<int:id>/', views.actualizar_terreno, name="act_terr" ),
    path('actualizar_coordinación/<int:id>/', views.actualizar_coordinacion, name="act_coor" ),
    path('bnup/', views.bnup, name="bnup" ),
    path('iniciativa/<int:pk>/detalles/', views.get_iniciativa_details, name='iniciativa_detalles'),
    path('error/', views.menu_1, name="menu_1" ),
    path("eliminar_bnup/", views.eliminar_bnup, name="eliminar_bnup")


]
