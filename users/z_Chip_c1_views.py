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
from z_Chip_c2_methods import ListChipDetails_Method



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
                tipodeconta = RetornNiveisComparation(sessaoUser.nivel)
                nivelValido = tipodeconta.Adm or tipodeconta.MeP or tipodeconta.Prj
                if nivelValido:
                    response.append(ResponseStandart(True))
                    pagina = request.data[1].get("page")
                    search = request.data[1].get("search")
                    categ  = request.data[1].get("categ")
                    arraydechips = ListChip_Method(pagina,search,categ,"s")
                    response.append(arraydechips)
                    arraycomplementar = ListChipDetails_Method(arraydechips)
                    response.append(arraycomplementar)
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