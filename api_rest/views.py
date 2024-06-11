from django.shortcuts import render

from django.http import HttpResponse ,JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer

import json

#primeira funcao para acessar dados
@api_view(['GET'])
def get_users(request):
    if request.method == 'GET':
        users = User.objects.all()
        
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_by_nick(request, nick):
    try:
        user = User.objects.get(user_nickname=nick)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        
        serializer = UserSerializer(user)


#CRUD 
@api_view(['GET','POST', 'PUT', 'DELETE'])
def userManager(request):
    # ACESSOS

    if request.method == 'GET':

        try:
            if request.GET['user']:                         # Check if there is a get parameter called 'user' (/?user=xxxx&...)

                user_nickname = request.GET['user']         # Find get parameter

                try:
                    user = User.objects.get(pk=user_nickname)   # Get the object in database
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)

                serializer = UserSerializer(user)           # Serialize the object data into json
                return Response(serializer.data)            # Return the serialized data

            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    

# CRIANDO DADOS

    if request.method == 'POST':

        new_user = request.data
        
        serializer = UserSerializer(data=new_user)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        return Response(status=status.HTTP_400_BAD_REQUEST)




# EDITAR DADOS (PUT)

    if request.method == 'PUT':

        nickname = request.data['user_nickname']

        try:
            updated_user = User.objects.get(pk=nickname)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        

        serializer = UserSerializer(updated_user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)




# DELETAR DADOS (DELETE)

    if request.method == 'DELETE':

        try:
            user_to_delete = User.objects.get(pk=request.data['user_nickname'])
            user_to_delete.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)














# Create your views here.
#desenvolver o crud da nossa aplicação
# def databaseEmDjango():
    
    
#     data= User.objects.get(pk='user_nickname')  #devolve um objeto
    
#     data = User.objects.filter(user_age = '20') #retornar queryset
    
#     data = User.objects.exclude(user_age = '25') #retorna todos os objetos que nao possuem o parametro fornecido retorna queryset
    
#     objects = []
#     for obj in data:
#         objects.append()
    
#     len(objects)
    
#     data.save() #salvar um objeto
    
#     data.delete() #deletar um objeto