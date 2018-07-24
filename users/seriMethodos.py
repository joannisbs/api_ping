# -*- coding: utf-8 -*-
import hashlib

def GeraTokenRetorno(psw,time):
    string = psw + time
    token = hashlib.sha256()
    token.update(string)
    token = str(token.hexdigest())
    return token

def GeraTokenSession(token,nivel,user):
    string = token + nivel + user
    token = hashlib.sha256()
    token.update(string)
    token = str(token.hexdigest())
    return token


def decodificatipodeconta(valor):
        if valor == 1:
            return 'Administrador'

        elif valor ==2:
            return 'MóduloProjeto'
        
        elif valor ==3:
            return 'Módulo'
        
        elif valor ==4:
            return 'Projeto'

        elif valor ==5:
            return 'Expedição'
        
        elif valor ==7:
            return 'Suporte'
        
   