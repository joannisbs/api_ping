#imports Relacionados ao Banco:
from users.models import User, Sessionini
from z_obj_User import Get_ListUsersPersonObject
from z_obj_User import Get_ListUsersSizeObject


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

        
def Get_SizeofListofUsers(page,filter):
    fimPaginacao  = int(page) * 25
    initPaginacao = fimPaginacao - 25
    
    if filter == 'all':
         sizeofListofUsers = len(User.objects
        .filter(user_ativo='s'))
            
    else:
        sizeofListofUsers = len(User.objects
        .filter(user_nome__icontains=filter, user_ativo='s'))
    

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

def Get_ListofUsers(page,filter):
    fimPaginacao  = int(page) * 25
    initPaginacao = fimPaginacao - 25
    ToBeSearch = False

    response = []

    if filter == 'all':
        result = (User.objects
            .filter(user_ativo='s')
            .order_by("user_nome")[initPaginacao:fimPaginacao])
    else:
        result = (User.objects
            .filter(user_nome__icontains=filter,user_ativo='s')
            .order_by("user_nome")[initPaginacao:fimPaginacao])

    for item in result:
        ToBeSearch = True
        person      = Get_ListUsersPersonObject()
        person.ids  = item.id 
        person.user = item.user_nome
        person.type = item.user_tipe
        response.append(person)
    if True:
        return response
    return False
