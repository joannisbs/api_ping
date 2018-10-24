# -*- coding: utf-8 -*-
def RetornaType (index):
    tipo = str(index)
    response = 'erro'
    if tipo == '1':
        response = "Administrador"      
    elif tipo =='2':
        response = u"Módulo e Projetos"
    elif tipo =='3':
        response = u"Módulo"
    elif tipo =='4':
        response = "Projetos"
    elif tipo =='5':
        response = u"Expedição"
    elif tipo =='6':
        response = " erro "
    elif tipo =='7':
        response = "Suporte"

    return response

def RetornNiveisComparation(nivel):
    response = nivels()
    tipo = str(nivel)
    
    if tipo == '1':
        response.Adm = True      
    elif tipo =='2':
        response.MeP = True 
    elif tipo =='3':
        response.Mod = True 
    elif tipo =='4':
        response.Prj = True
    elif tipo =='5':
        response.Exp = True 
    elif tipo =='7':
        response.Sup = True 

    return response

class nivels:
    def __init__(self):
        self.Adm   = False
        self.Mod   = False
        self.MeP   = False
        self.Prj   = False
        self.Exp   = False
        self.Sup   = False

def ArrumaData(data):
    dataarrumada = data
  
    if '/' in data:
        dado = data.split('/')
        if len(dado) == 3:
            if len(dado[2])==1:
                dado[2] = ''
            if len(dado[0])==1:
                dado[0] = '0' + dado[0]
            if len(dado[2])==3:
                dado[2] = ''
            if len(dado[2])==4:
                dado[2] = dado[2][2] + dado[2][3]
            dataarrumada = dado[2] + "_" + dado[1] + "_" + dado [0]
        elif len(dado) == 2:
            if len(dado[1])==1:
                dado[1] = ''
            if len(dado[0])==1:
                dado[0] = '0' + dado[0]
            dataarrumada = dado[1] + "_" + dado [0]
        else:
            dataarrumada = data
  
    return dataarrumada  

class Post_historyObject:
    def __init__(self):
        self.ids            = ''
        self.hora           = ''
        self.event          = ''