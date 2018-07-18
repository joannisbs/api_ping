# -*- coding: utf-8 -*-
import hashlib
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
#from snippets.models import Snippet
from users.serializers import UserSerializer, RespSerializers
from users.models import User


@api_view(['GET', 'POST'])
def Userlogin(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        instance = serializer.Desmonta(request.data)
        psw= hashlib.md5()
        psw.update(instance.word)
        psw = str(psw.hexdigest())
        res = serializer.Authentic(instance.user,psw)
        
        if (res[0]==True):
            
            resp = serializer.IniciaSessao(psw,res[1],res[2],instance.user)
            seri = RespSerializers(resp)
            resp = serializer.RespSerializer(seri.data)
            return Response(resp)
        else:
            resp = serializer.BadLogin(instance.user)
            seri = RespSerializers(resp)
            resp = serializer.RespSerializer(seri.data)
            return Response(resp)


"""
    List all code snippets, or create a new snippet.
    
    if request.method == 'GET':


        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        """