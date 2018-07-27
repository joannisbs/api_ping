#imports Relacionados ao Banco:
from users.models import User, Sessionini


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