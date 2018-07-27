# -*- coding: utf-8 -*-
#import hashlib
# Imports Framework
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

#import da Interface.
from z1_interface_User import R_Userlogin_Interface
from z1_interface_User import R_GetTokenfromClient
from z2_methods_User import ValidSession_Method

#imports da camada de Methodos.
from z2_methods_User import Userlogin_Method

@api_view(['POST'])
def Userlogin_View(request):
    if request.method == 'POST':
        try:
            TentativaLogin = R_Userlogin_Interface(request.data)
            return Response (Userlogin_Method (TentativaLogin))
        except:
            return Response (404)


@api_view(['POST'])
def ListUsers(request):
    if request.method == 'POST':
        sessaoUser = R_GetTokenfromClient(request.data[0])
        sessaovalida = ValidSession_Method(sessaoUser)
        if sessaovalida:
            print "Valida"
        print "Invalida"


#     if request.method == 'POST':
#         tokens = RespSerializers(request.data[0])
#         #print tokens.data
#         sessaovalida = tokens.ValidaSession(tokens.data)
#         if sessaovalida[0]:
#             resp = getListUsers(request.data[1],request.data[2])
#             return Response(resp)



# @api_view(['POST'])
# def NewUser(request):
#     if request.method == 'POST':
#         tokens = RespSerializers(request.data[0])
#         #print tokens.data
#         sessaovalida = tokens.ValidaSession(tokens.data)
#         dado = newUserSerializer(request.data[1])
#         if sessaovalida[0]:
#             resposta = dado.createUser(dado.data,sessaovalida[1])
#             resposta = respNewUserSerializers(resposta)
#             return Response(resposta.data)
#         else:
#             respostas.newUser_resp(False,3) 
#             resposta = respNewUserSerializers(resposta)
#             return Response(resposta.data)

# 

# @api_view(['POST'])
# def historyUsers(request):
#     if request.method == 'POST':
#         tokens = RespSerializers(request.data[0])
#         #print tokens.data
#         sessaovalida = tokens.ValidaSession(tokens.data)
#         if sessaovalida[0]:
#             resp = HistoryUsuario(request.data[1],request.data[2],request.data[3])
#             return Response(resp)

# @api_view(['POST'])
# def DeleteUser(request):
#     if request.method == 'POST':
#         tokens = RespSerializers(request.data[0])
#         sessaovalida = tokens.ValidaSession(tokens.data)
#         if sessaovalida[0]:
#             print request.data[1]
#             resp = DeleteUsuario(request.data[1])
            
#             return Response(resp)