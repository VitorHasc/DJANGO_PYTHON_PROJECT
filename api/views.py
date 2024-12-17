from django.contrib.auth.hashers import check_password
from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Pessoa
from .serializers import PessoaSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password


@api_view(['GET'])
def getData(request):
    pessoas = Pessoa.objects.all()
    serializer = PessoaSerializer(pessoas, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addData(request):
    data = request.data
    data['senha'] = make_password(data['senha'])
    serializer = PessoaSerializer(data=data)
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteData(request, pk):
    try:
        pessoa = Pessoa.objects.get(pk=pk)
    except Pessoa.DoesNotExist:
        return Response({"detail": "Not found."}, status=404)
    
    pessoa.delete()
    return Response({"detail": "Deleted successfully."}, status=204)


@api_view(['PUT'])
def updateData(request, pk):
    try:
        pessoa = Pessoa.objects.get(pk=pk)
    except Pessoa.DoesNotExist:
        return Response({"detail": "Not found."}, status=404)
    
    serializer = PessoaSerializer(pessoa, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors, status=400)


@api_view(['POST'])
def login(request):
    pessoas = Pessoa.objects.all()
    serializer = PessoaSerializer(pessoas, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    senha = request.data.get('senha')
    pessoa = Pessoa.objects.get(email=email)
    if check_password(senha, pessoa.senha):
        refresh = RefreshToken.for_user(pessoa)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        })
    
    else:
        return Response({"detail": "Credenciais inválidas."}, status=401)