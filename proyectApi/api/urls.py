from django.urls import path
from django.urls import path
from .views import agregarUsuario, buscar_Usuario, editarUsuario, eliminarUsuario, listar_Usuario

urlpatterns = [
    path('listar/', listar_Usuario),
    path('agregar/', agregarUsuario),
    path('editar/<p_id>', editarUsuario),
    path('eliminar/<p_id>', eliminarUsuario),
    path('buscar/<id>', buscar_Usuario),
]