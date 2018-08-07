
def RetornaType (index):
    tipo = str(index)
    response = 'erro'
    if tipo == '1':
        response = "Administrador"      
    elif tipo =='2':
        response = "Modulo e Projetos"
    elif tipo =='3':
        response = "Modulo"
    elif tipo =='4':
        response = "Projetos"
    elif tipo =='5':
        response = "Expedicao"
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
       