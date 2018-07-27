from users.models import User, Sessionini

def Updt_SessiontoInvalid(ids):
    try:
        peaple =  Sessionini.objects.filter(user_ids = ids)
        # Existe Apenas um usuario com este nome no banco. 
        for person in peaple:
            person.ativo = False
            person.save()
    except:
        print "ERRO AO INVALIDAR SESSAO"
        return False