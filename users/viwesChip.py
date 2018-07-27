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