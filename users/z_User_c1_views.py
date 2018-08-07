# -*- coding: utf-8 -*-
#import hashlib
# Imports Framework
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

#import da Interface.
from z_User_c1_interface import R_AlterTypeUser_Interface
from z_User_c1_interface import R_GetListhistoryUser_Interface
from z_User_c1_interface import R_GetListUser_Interface
from z_User_c1_interface import R_GetTokenfromClient_Interface
from z_User_c1_interface import R_NewUser_Interface
from z_User_c1_interface import R_Userlogin_Interface

#imports da camada de Methodos.
from z_User_c2_methods import AlterTypeUser_Method
from z_User_c2_methods import CreateUser_Method
from z_User_c2_methods import DeleteUser_Method
from z_User_c2_methods import GethistoryUser_Method
from z_User_c2_methods import GetListUser_Method
from z_User_c2_methods import NewPass_Method
from z_User_c2_methods import Reactivate_user_Method
from z_User_c2_methods import ReposnseTokenError
from z_User_c2_methods import ResetUser_Method
from z_User_c2_methods import ResponseStandart
from z_User_c2_methods import ResponseStandartWithMotive
from z_User_c2_methods import ValidSession_Method
from z_User_c2_methods import Userlogin_Method



@api_view(['POST'])
def Userlogin_View(request):
    if request.method == 'POST':
        try:
            TentativaLogin = R_Userlogin_Interface(request.data)
            return Response (Userlogin_Method (TentativaLogin))
        except:
            return Response (404)
    else:
        return Response (403)


@api_view(['POST'])
def GetHystoryUser_View(request):
    if request.method == 'POST':
        try:
            sessaoUser = R_GetTokenfromClient_Interface(request.data[0])
           
            sessaovalida = ValidSession_Method(sessaoUser)
            if sessaovalida:
                filtros = R_GetListhistoryUser_Interface(request.data[1])
                return Response(GethistoryUser_Method(filtros.ids,filtros.page,filtros.filtro))

            else:
                return Response(ReposnseTokenError())
        
               
        except:
            return Response (403)


@api_view(['POST'])
def ListUsers_View(request):
    if request.method == 'POST':
        try:
            sessaoUser = R_GetTokenfromClient_Interface(request.data[0])
            sessaovalida = ValidSession_Method(sessaoUser)
            if sessaovalida:
                filtros = R_GetListUser_Interface(request.data[1])
                return Response(GetListUser_Method(filtros,True))
            return Response(ReposnseTokenError())
        except:
            return Response (403)

@api_view(['POST'])
def DesactivateListUsers_View(request):
    if request.method == 'POST':
        try:
            sessaoUser = R_GetTokenfromClient_Interface(request.data[0])
            sessaovalida = ValidSession_Method(sessaoUser)
            if sessaovalida:
                filtros = R_GetListUser_Interface(request.data[1])
                return Response(GetListUser_Method(filtros,False))
            return Response(ReposnseTokenError())
        except:
            return Response (403)

@api_view(['POST'])
def EditUserType_View(request):
    response = []
    if request.method == 'POST':
        try:
            sessaoUser = R_GetTokenfromClient_Interface(request.data[0])
            if sessaoUser.nivel == '1':
                sessaovalida = ValidSession_Method(sessaoUser)
                if sessaovalida:
                    response.append(ResponseStandart(True))
                    person = R_AlterTypeUser_Interface(request.data[1])
                    sucess = AlterTypeUser_Method ( sessaoUser.ids, 
                                                        person.ids, person.type)
                    
                    if sucess:
                        response.append(ResponseStandart(True))
                        return Response (response)
                    else:
                        response.append(ResponseStandart(False))
                        return Response (response)
                else:
                    return Response(ReposnseTokenError())
            else:
                return Response(ReposnseTokenError())
        except:
            return Response (403)

@api_view(['POST'])
def ResetPasswordStandart_View(request):
    response = []
    if request.method == 'POST':
        try:
            sessaoUser = R_GetTokenfromClient_Interface(request.data[0])
            if sessaoUser.nivel == '1':
                sessaovalida = ValidSession_Method(sessaoUser)
                if sessaovalida:
                    response.append(ResponseStandart(True))
                    iduser = request.data[1]
                    sucess = ResetUser_Method(sessaoUser.ids, iduser)
                    if sucess:
                        response.append(ResponseStandart(True))
                        return Response (response)
                    else:
                        response.append(ResponseStandart(False))
                        return Response (response)
                else:
                    return Response(ReposnseTokenError())
            else:
                return Response(ReposnseTokenError())
        except:
            return Response (403)



@api_view(['POST'])
def DeleteUser_View(request):
    response = []
    if request.method == 'POST':
        try:
            sessaoUser = R_GetTokenfromClient_Interface(request.data[0])
            if sessaoUser.nivel == '1':
                sessaovalida = ValidSession_Method(sessaoUser)
                if sessaovalida:
                    response.append(ResponseStandart(True))
                    iduser = request.data[1]
                    sucess = DeleteUser_Method(sessaoUser.ids, iduser)
                    if sucess:
                        response.append(ResponseStandart(True))
                        return Response (response)
                    else:
                        response.append(ResponseStandart(False))
                        return Response (response)
                else:
                    return Response(ReposnseTokenError())
            else:
                return Response(ReposnseTokenError())
        except:
            return Response (403)

@api_view(['POST'])
def ReactivateUser_View(request):
    response = []
    if request.method == 'POST':
        try:
            sessaoUser = R_GetTokenfromClient_Interface(request.data[0])
            if sessaoUser.nivel == '1':
                sessaovalida = ValidSession_Method(sessaoUser)
                if sessaovalida:
                    response.append(ResponseStandart(True))
                    iduser = request.data[1]
                    sucess = Reactivate_user_Method(sessaoUser.ids, iduser)
                    if sucess:
                        response.append(ResponseStandart(True))
                        return Response (response)
                    else:
                        response.append(ResponseStandart(False))
                        return Response (response)
                else:
                    return Response(ReposnseTokenError())
            else:
                return Response(ReposnseTokenError())
        except:
            return Response (403)




@api_view(['POST'])
def NewUser_View(request):
    response = []
    if request.method == 'POST':
        try:
            sessaoUser = R_GetTokenfromClient_Interface(request.data[0])
            sessaovalida = ValidSession_Method(sessaoUser)
            if sessaovalida:
                response.append(ResponseStandart(True))
                if sessaoUser.nivel == '1':
                    response.append(ResponseStandart(True))
                    UserRequest = R_NewUser_Interface(request.data[1])
                    sucessSave = CreateUser_Method(sessaoUser.ids,UserRequest.user, UserRequest.type)
                    if sucessSave == 1:
                        response.append(ResponseStandart(True))
                    else:
                        response.append(ResponseStandartWithMotive(False,sucessSave))
                    return Response (response)
            return Response(ReposnseTokenError())
        except:
            return Response (403)      
    return Response (403)


@api_view(['POST'])
def NewPassword_View(request):
    response = []
    if request.method == 'POST':
        try:
            sessaoUser = R_GetTokenfromClient_Interface(request.data[0])
            sessaovalida = ValidSession_Method(sessaoUser)
            if sessaovalida:
                response.append(ResponseStandart(True))
                password = request.data[1]
                if NewPass_Method(sessaoUser.ids,password):
                    response.append(ResponseStandart(True))
                    return Response(response)
            response.append(ResponseStandart(False))
            return Response(response)
        except:
            response.append(ResponseStandart(False))
            response.append(ResponseStandart(False))
            return Response(response)