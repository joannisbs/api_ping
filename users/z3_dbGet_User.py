#imports Relacionados ao Banco:
from users.models import User


def Get_UserActivesForLogin(userName):
    try:
        peaple =   (User.objects.filter(user_nome=userName,user_ativo='s')|
                    User.objects.filter(user_nome=userName,user_ativo='A'))
        # Existe Apenas um usuario com este nome no banco. 
        for person in peaple:
            return person
    except:
        return False