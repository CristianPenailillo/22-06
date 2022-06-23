from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .models import Usuario
from .serializers import UsuarioSerializer


@csrf_exempt
@api_view(['GET'])
def listar_Usuario(request):
    
    usuario = Usuario.objects.all()
    serializer = UsuarioSerializer(usuario, many=True)
    return Response(serializer.data)

@csrf_exempt
@api_view(['GET'])
def buscar_Usuario(request, id):
    
    usuario = Usuario.objects.filter(id=id)
    serializer = UsuarioSerializer(usuario, many=True)
    return Response(serializer.data)


@csrf_exempt
@api_view(['POST'])
def agregarUsuario(request):
    Usuario.objects.create(
        nombre=request.POST['nombre'],
        apellido=request.POST['apellido'],
        edad=request.POST['edad']
    )
    
    return Response([{"mensaje": "Se Agrego el usuario Correctamente"}])


@csrf_exempt
@api_view(['PUT'])
def editarUsuario(request, p_id):

        usuario = Usuario.objects.get(id=p_id)

        usuario.nombre=request.POST['nombre']
        usuario.apellido=request.POST['apellido']
        usuario.edad=request.POST['edad']

        usuario.save()

        return Response([{"mensaje": "Se Modifico Correctamente"}])

    


@csrf_exempt
@api_view(['DELETE'])
def eliminarUsuario(request, p_id):
    try:
        usuario = Usuario.objects.get(id=p_id)

        usuario.delete()
        return Response([{"mensaje": "Se Elimino Correctamente"}])

    except usuario.DoesNotExist:
        return Response(Usuario.errors, status=status.HTTP_400_BAD_REQUEST)
