#imports Relacionados ao Banco:
from users.models import User, Sessionini
from z_obj_User import Get_ListUsersPersonObject
from z_obj_User import Get_ListUsersSizeObject
from z_obj_User import Post_historyUserObject
from users.models import HistoryUser
from django.db.models import Q

def Get_UserActivesForLogin(userName):
    try:
        peaple =   (User.objects.filter(user_nome=userName,user_ativo='s')|
                    User.objects.filter(user_nome=userName,user_ativo='A'))
        # Existe Apenas um usuario com este nome no banco. 
        for person in peaple:
            return person
    except:
        return False
    
def Get_SessionValid(ids):
    try:
        peaple =  Sessionini.objects.filter(user_ids = ids,ativo=True)
        # Existe Apenas um usuario com este nome no banco. 
        for person in peaple:
            personMaisNovo = person
        return personMaisNovo
    except:
        return False

def Get_ListofHistoryUsers(iduser,page,filter):
    
    fimPaginacao  = int(page) * 50
    initPaginacao = fimPaginacao - 50
    ToBeSearch = False

    response = []

    if filter == 'all':
        result = (HistoryUser.objects.filter(user_ids=iduser).order_by('-hora')[initPaginacao:fimPaginacao])
    else:
        result = (HistoryUser.objects.filter(Q(
            event__icontains=filter, user_ids=iduser)|
            Q(hora__icontains=filter, user_ids=iduser)).order_by('-hora'))[initPaginacao:fimPaginacao]


    for item in result:
        ToBeSearch = True
        history      = Post_historyUserObject()
        history.event = item.event
        history.hora = item.hora
        response.append(history)
    if ToBeSearch:
        return response
    return False

def Get_SizeHistoryofUsers (iduser,page,filter):   

    fimPaginacao  = int(page) * 50
    initPaginacao = fimPaginacao - 50
    
    if filter == 'all':
         sizeofListofHistoryUsers = len(HistoryUser.objects.filter(user_ids=iduser))
            
    else:
        sizeofListofHistoryUsers = len(HistoryUser.objects.filter(Q(
            event__icontains=filter, user_ids=iduser)|
            Q(hora__icontains=filter, user_ids=iduser)))
    

    toBeNext = 0

    if fimPaginacao  > sizeofListofHistoryUsers:
        fimPaginacao = sizeofListofHistoryUsers
        toBeNext = 1
    response = Get_ListUsersSizeObject()
    response.initpag = initPaginacao
    response.endpag  = fimPaginacao
    response.size    = sizeofListofHistoryUsers
    response.next    = toBeNext
    return response

def Get_SizeofListofUsers(page,filter,condicion):
    if condicion:
        ativos = 's'
    else:
        ativos = 'n'

    fimPaginacao  = int(page) * 25
    initPaginacao = fimPaginacao - 25
    
    if filter == 'all':
         sizeofListofUsers = len(User.objects
        .filter(user_ativo=ativos))
            
    else:
        sizeofListofUsers = len(User.objects
        .filter(user_nome__icontains=filter, user_ativo=ativos))
    

    toBeNext = 0

    if fimPaginacao>sizeofListofUsers:
        fimPaginacao=sizeofListofUsers
        toBeNext = 1
    response = Get_ListUsersSizeObject()
    response.initpag = initPaginacao
    response.endpag  = fimPaginacao
    response.size    = sizeofListofUsers
    response.next    = toBeNext
    return response
    
def Get_UserById(ids):
    result = User.objects.filter(id=ids)
    for item in result:
        return item.user_nome

def Get_ListofUsers(page,filter,condicion):
    if condicion:
        ativos = 's'
    else:
        ativos = 'n'

    fimPaginacao  = int(page) * 25
    initPaginacao = fimPaginacao - 25
    ToBeSearch = False

    response = []

    if filter == 'all':
        result = (User.objects
            .filter(user_ativo=ativos)
            .order_by("user_nome")[initPaginacao:fimPaginacao])
    else:
        result = (User.objects
            .filter(user_nome__icontains=filter,user_ativo=ativos)
            .order_by("user_nome")[initPaginacao:fimPaginacao])

    for item in result:
        ToBeSearch = True
        person      = Get_ListUsersPersonObject()
        person.ids  = item.id 
        person.user = item.user_nome
        person.type = item.user_tipe
        response.append(person)
    if ToBeSearch:
        return response
    return False

def Get_checkUserExists(name):
    result = User.objects.filter(user_nome = name)
    for item in result:
        return False
    
    return True