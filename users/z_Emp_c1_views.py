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

from z__Dicts import Dict_respostas_Post
from z__Dicts import Dict_respostas_Session

from z_Emp_c2_methods import NewCompany_Method
from z_Emp_c2_methods import ListCompany_Method
from z_Emp_c2_methods import DeleteCompany_Method
from z_Emp_c2_methods import ActiveCompany_Method
from z_Emp_c2_methods import EditCompany_Method
from z_Emp_c2_methods import ListHistoryCompany_Method

@api_view(['POST'])
def EditEmp_View(request):
    resptofront = []
    respSess  = 'inicializado'
    respPost    = 'inicializado'

    if request.method == 'POST':      
        try:
            sessaoUser   = R_GetTokenfromClient_Interface ( request.data[0] )
            sessaoValida = ValidSession_Method ( sessaoUser )

            if sessaoValida:
                tipodeconta = RetornNiveisComparation ( sessaoUser.nivel )
                nivelValido = tipodeconta.Adm or tipodeconta.MeP or tipodeconta.Mod 

                if nivelValido:
                    respSess = 'sucesso'
                    respPost = EditCompany_Method   ( request.data[1], request.data[2], sessaoUser.ids )
                    respPost = Dict_respostas_Post [ respPost ]
                
                else:
                    respSess = 'acessoNegado'    
            
            else:
                respSess = 'sessaoInvalida'        
        except:
            
            respSess = 'erroDesconhecido'  
    else:
        respSess = 'erroDesconhecido' 
    
    respSess = Dict_respostas_Session [ respSess ]

    resptofront.append ( respSess )
    resptofront.append ( respPost )
    
    return Response ( resptofront )


@api_view(['POST'])
def NewEmp_View(request):
    resptofront = []
    respSess  = 'inicializado'
    respPost    = 'inicializado'

    if request.method == 'POST':      
        
        sessaoUser   = R_GetTokenfromClient_Interface ( request.data[0] )
        sessaoValida = ValidSession_Method ( sessaoUser )

        if sessaoValida:
            tipodeconta = RetornNiveisComparation ( sessaoUser.nivel )
            nivelValido = tipodeconta.Adm or tipodeconta.MeP or tipodeconta.Mod 

            if nivelValido:
                respSess = 'sucesso'
                respPost = NewCompany_Method   ( request.data[1], sessaoUser.ids )
                respPost = Dict_respostas_Post [ respPost ]
            
            else:
                respSess = 'acessoNegado'    
        
        else:
            respSess = 'sessaoInvalida'        
       
    else:
        respSess = 'erroDesconhecido' 
    
    respSess = Dict_respostas_Session [ respSess ]

    resptofront.append ( respSess )
    resptofront.append ( respPost )
    
    return Response ( resptofront )



@api_view(['POST'])
def ListEmpActive_View ( request ):
    resptofront = []
    respSess  = 'inicializado'

    if request.method == 'POST':      
        try:
            sessaoUser   = R_GetTokenfromClient_Interface ( request.data[0] )
            sessaoValida = ValidSession_Method ( sessaoUser )

            if sessaoValida:
                
                nivelValido = True # Todos os níveis tem permissão para visualizar

                if nivelValido:
                    respSess = 'sucesso'
                    respMeth = ListCompany_Method   ( request.data[1], True )
                
                else:
                    respSess = 'acessoNegado'    
            
            else:
                respSess = 'sessaoInvalida'        
        except:
            
            respSess = 'erroDesconhecido'  
    else:
        respSess = 'erroDesconhecido' 
    
    respSess = Dict_respostas_Session [ respSess ]

    resptofront.append ( respSess )
    resptofront.extend ( respMeth )

    return Response ( resptofront )

@api_view(['POST'])
def ListEmpDesactive_View ( request ):
    resptofront = []
    respSess  = 'inicializado'

    if request.method == 'POST':      
        try:
            sessaoUser   = R_GetTokenfromClient_Interface ( request.data[0] )
            sessaoValida = ValidSession_Method ( sessaoUser )

            if sessaoValida:
                
                nivelValido = True # Todos os níveis tem permissão para visualizar

                if nivelValido:
                    respSess = 'sucesso'
                    respMeth = ListCompany_Method   ( request.data[1], False )
                
                else:
                    respSess = 'acessoNegado'    
            
            else:
                respSess = 'sessaoInvalida'        
        except:
            
            respSess = 'erroDesconhecido'  
    else:
        respSess = 'erroDesconhecido' 
    
    respSess = Dict_respostas_Session [ respSess ]

    resptofront.append ( respSess )
    resptofront.extend ( respMeth )
    
    
    return Response ( resptofront )

@api_view(['POST'])
def ListHistoryEmp_View ( request ):
    resptofront = []
    respSess  = 'inicializado'
    respMeth  = 'inicializado'

    if request.method == 'POST':      
        try:
            sessaoUser   = R_GetTokenfromClient_Interface ( request.data[0] )
            sessaoValida = ValidSession_Method ( sessaoUser )

            if sessaoValida:
                
                nivelValido = True # Todos os níveis tem permissão para visualizar

                if nivelValido:
                    respSess = 'sucesso'
                    respMeth = ListHistoryCompany_Method   ( request.data[1])
                else:
                    respSess = 'acessoNegado'    
            
            else:
                respSess = 'sessaoInvalida'        
        except:
            
            
            respSess = 'erroDesconhecido'  
    else:
        respSess = 'erroDesconhecido' 
    
    respSess = Dict_respostas_Session [ respSess ]

    resptofront.append ( respSess )
    resptofront.extend ( respMeth )

    return Response ( resptofront )

@api_view(['POST'])
def ToDesactive_View ( request ):
    resptofront = []
    respSess  = 'inicializado'
    respPost    = 'inicializado'

    if request.method == 'POST':      
        try:
            sessaoUser   = R_GetTokenfromClient_Interface ( request.data[0] )
            sessaoValida = ValidSession_Method ( sessaoUser )

            if sessaoValida:
                tipodeconta = RetornNiveisComparation ( sessaoUser.nivel )
                nivelValido = tipodeconta.Adm or tipodeconta.MeP or tipodeconta.Mod 

                if nivelValido:
                    respSess = 'sucesso'
                    respPost = DeleteCompany_Method   ( request.data[1], sessaoUser.ids )
                    respPost = Dict_respostas_Post [ respPost ]
                
                else:
                    respSess = 'acessoNegado'    
            
            else:
                respSess = 'sessaoInvalida'        
        except:
            
            respSess = 'erroDesconhecido'  
    else:
        respSess = 'erroDesconhecido' 
    
    respSess = Dict_respostas_Session [ respSess ]

    resptofront.append ( respSess )
    resptofront.append ( respPost )
    
    return Response ( resptofront )

@api_view(['POST'])
def ToReactive_View ( request ):
    resptofront = []
    respSess    = 'inicializado'
    respPost    = 'inicializado'

    if request.method == 'POST':      
        try:
            sessaoUser   = R_GetTokenfromClient_Interface ( request.data[0] )
            sessaoValida = ValidSession_Method ( sessaoUser )

            if sessaoValida:
                tipodeconta = RetornNiveisComparation ( sessaoUser.nivel )
                nivelValido = tipodeconta.Adm or tipodeconta.MeP or tipodeconta.Mod 

                if nivelValido:
                    respSess = 'sucesso'
                    respPost = ActiveCompany_Method   ( request.data[1], sessaoUser.ids )
                    respPost = Dict_respostas_Post [ respPost ]
                
                else:
                    respSess = 'acessoNegado'    
            
            else:
                respSess = 'sessaoInvalida'        
        except:
            
            respSess = 'erroDesconhecido'  
    else:
        respSess = 'erroDesconhecido' 
    
    respSess = Dict_respostas_Session [ respSess ]

    resptofront.append ( respSess )
    resptofront.append ( respPost )
    
    return Response ( resptofront )

