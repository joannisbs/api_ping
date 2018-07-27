# -*- coding: utf-8 -*-
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from users.seriResp import RespSerializers

from users.seriChip import createChip


import respostas

@api_view(['POST'])
def newChip(request):
    if request.method == 'POST':
        tokens = RespSerializers(request.data[0])
        #print tokens.data
        sessaovalida = tokens.ValidaSession(tokens.data)
        if sessaovalida[0]:
            listOfChips = request.data[1].get('chips')
            respostas = []
            for item in listOfChips:
                resposta = createChip(item,sessaovalida[1])
                respostas.append(resposta)
            print respostas
            return Response(respostas)



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