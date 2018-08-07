
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