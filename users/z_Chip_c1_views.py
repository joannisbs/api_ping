# -*- coding: utf-8 -*-
#import hashlib
# Imports Framework
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

#importes referentes aos modulos de usuários
from z_User_c1_interface import R_GetTokenfromClient_Interface

from z_User_c2_methods import ResponseStandart
from z_User_c2_methods import ValidSession_Method
from z_User_c2_methods import ReposnseTokenError

#Ferramentas
from z__functionsgenericas import RetornNiveisComparation

# Imports de Interfaces
from z_Chip_c1_interface import R_GetNewChip_Interface 

#imports de Methods
from z_Chip_c2_methods import CreateChip_method 
from z_Chip_c2_methods import ListChip_Method
from z_Chip_c2_methods import DeletChip_method
from z_Chip_c2_methods import ActivChip_method 
from z_Chip_c2_methods import EditIpChip_method 


@api_view(['POST'])
def NewChip_View(request):
    response = []
    if request.method == 'POST':
        try:
            sessaoUser = R_GetTokenfromClient_Interface(request.data[0])
            sessaovalida = ValidSession_Method(sessaoUser)
            if sessaovalida:
                response.append(ResponseStandart(True))
                tipodeconta = RetornNiveisComparation(sessaoUser.nivel)
                nivelValido = tipodeconta.Adm or tipodeconta.MeP or tipodeconta.Prj
                if nivelValido:
                    response.append(ResponseStandart(True))
                    listOfChips = request.data[1].get('chips')
                    respostasdoschips = []
                    for item in listOfChips:
                        chip = R_GetNewChip_Interface (item)
                        resposta = CreateChip_method(sessaoUser.ids,chip)
                        respostasdoschips.append(resposta)
                    response.append(respostasdoschips)
                    return Response(response)
                else:
                    response.append(ResponseStandart(False))
                    response.append(ResponseStandart(False))
                    return Response(response)
            else:
                return Response(ReposnseTokenError())
        except:
            return Response(ReposnseTokenError())
    return Response(ReposnseTokenError())

@api_view(['POST'])
def ListChip_View(request):
    response = []
    if request.method == 'POST':
        try:
            sessaoUser = R_GetTokenfromClient_Interface(request.data[0])
            sessaovalida = ValidSession_Method(sessaoUser)
            if sessaovalida:
                response.append(ResponseStandart(True))
                nivelValido = True
                if nivelValido:
                    response.append(ResponseStandart(True))
                    pagina = request.data[1].get("page")
                    search = request.data[1].get("search")
                    categ  = request.data[1].get("categ")
                    arraydechips = ListChip_Method(pagina,search,categ,"s")
                    response.append(arraydechips)
                    return Response(response)
                else:
                    response.append(ResponseStandart(False))
                    response.append(ResponseStandart(False))
                    return Response(response)
            else:
                return Response(ReposnseTokenError())
        except:
            return Response(ReposnseTokenError())
    return Response(ReposnseTokenError())

@api_view(['POST'])
def listDesactivedChip_View(request):
    response = []
    if request.method == 'POST':
        try:
            sessaoUser = R_GetTokenfromClient_Interface(request.data[0])
            sessaovalida = ValidSession_Method(sessaoUser)
            if sessaovalida:
                response.append(ResponseStandart(True))
                tipodeconta = RetornNiveisComparation(sessaoUser.nivel)
                nivelValido = tipodeconta.Adm or tipodeconta.MeP or tipodeconta.Prj
                if nivelValido:
                    response.append(ResponseStandart(True))
                    pagina = request.data[1].get("page")
                    search = request.data[1].get("search")
                    categ  = request.data[1].get("categ")
                
                    arraydechips = ListChip_Method(pagina,search,categ,"n")
                    response.append(arraydechips)
                    return Response(response)
                else:
                    response.append(ResponseStandart(False))
                    response.append(ResponseStandart(False))
                    return Response(response)
            else:
                return Response(ReposnseTokenError())
        except:
            return Response(ReposnseTokenError())
    return Response(ReposnseTokenError())

@api_view(['POST'])
def EditIpChip_View(request):
    response = []
    if request.method == 'POST':
        try:
            sessaoUser = R_GetTokenfromClient_Interface(request.data[0])
            sessaovalida = ValidSession_Method(sessaoUser)
            if sessaovalida:
                response.append(ResponseStandart(True))
                tipodeconta = RetornNiveisComparation(sessaoUser.nivel)
                nivelValido = tipodeconta.Adm or tipodeconta.MeP or tipodeconta.Prj
                if nivelValido:
                    response.append(ResponseStandart(True))
                    chip_ip = request.data[1].get("chip_ip")
                    chip_oper = request.data[1].get("chip_oper")
                    chipid     = request.data[1].get("id")
                    chip_num = request.data[1].get("chip_num") 
                    
                    print chip_ip 
                    print chip_oper
                    print chipid
                    print chip_num
                    suces = EditIpChip_method(chipid,chip_ip,chip_oper,sessaoUser.ids,request.data[2])
                    response.append(ResponseStandart(suces))
                    print suces
                    return Response(response)
                else:
                    response.append(ResponseStandart(False))
                    response.append(ResponseStandart(False))
                    return Response(response)
            else:
                return Response(ReposnseTokenError())
        except:
            return Response(ReposnseTokenError())
    return Response(ReposnseTokenError())

@api_view(['POST'])
def ChipDelete_View(request):
    response = []
    if request.method == 'POST':
        try:
            sessaoUser = R_GetTokenfromClient_Interface(request.data[0])
            sessaovalida = ValidSession_Method(sessaoUser)
            if sessaovalida:
                response.append(ResponseStandart(True))
                tipodeconta = RetornNiveisComparation(sessaoUser.nivel)
                nivelValido = tipodeconta.Adm or tipodeconta.MeP or tipodeconta.Prj
                if nivelValido:
                    response.append(ResponseStandart(True))
                    chipid = request.data[1]
                    motivo = request.data[2]
                    if DeletChip_method(chipid, sessaoUser.ids, motivo):
                        response.append(ResponseStandart(True))

                    else:
                        response.append(ResponseStandart(False))
                    return Response(response)
                else:
                    response.append(ResponseStandart(False))
                    return Response(response)

               
            return Response(ReposnseTokenError())
        except:
            return Response (403)

@api_view(['POST'])
def ChipActive_View(request):
    response = []
    if request.method == 'POST':
        try:
            sessaoUser = R_GetTokenfromClient_Interface(request.data[0])
            sessaovalida = ValidSession_Method(sessaoUser)
            if sessaovalida:
                response.append(ResponseStandart(True))
                tipodeconta = RetornNiveisComparation(sessaoUser.nivel)
                nivelValido = tipodeconta.Adm or tipodeconta.MeP or tipodeconta.Prj
                if nivelValido:
                    response.append(ResponseStandart(True))
                    chipid = request.data[1]
                    motivo = request.data[2]
                    if ActivChip_method(chipid, sessaoUser.ids, motivo):
                        response.append(ResponseStandart(True))
                    else:
                        response.append(ResponseStandart(False))
                    return Response(response)
                else:
                    response.append(ResponseStandart(False))
                    return Response(response)

               
            return Response(ReposnseTokenError())
        except:
            return Response (403)