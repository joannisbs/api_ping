from users.models import User, Sessionini

def Updt_AlterTypeUser (ids, types):
    try:
        peaple =  User.objects.filter(id = ids)

        # Existe Apenas um usuario com este nome no banco. 
        for person in peaple:
    
            person.user_tipe = types
            person.save()
            return True
    except:
        return False




def Updt_SessiontoInvalid(ids):
    try:
        peaple =  Sessionini.objects.filter(user_ids = ids)
        # Existe Apenas um usuario com este nome no banco. 
        for person in peaple:
            person.ativo = False
            person.save()
        return True
    except:
        print "ERRO AO INVALIDAR SESSAO"
        return False
    
def Updt_DeleteUser(ids):
    try:
        peaple =  User.objects.filter(id = ids)

        # Existe Apenas um usuario com este nome no banco. 
        for person in peaple:
    
            person.user_ativo = 'n'
            person.save()
        return True
    except:
        return False
    
def Updt_ReactivateUser (ids):
    try:
        peaple =  User.objects.filter(id = ids)

        # Existe Apenas um usuario com este nome no banco. 
        for person in peaple:
    
            person.user_ativo = 's'
            person.save()
            return True
    except:
        return False

def Updt_ResetUser (ids):
    try:
        peaple =  User.objects.filter(id = ids)

        # Existe Apenas um usuario com este nome no banco. 
        for person in peaple:
    
            person.user_pass = "dd6e5e5918e94d997c686fcebc56922f"
            person.save()
            return True
    except:
        return False

def Updt_NewPass (ids, pws):
    try:
        peaple =  User.objects.filter(id = ids)

        # Existe Apenas um usuario com este nome no banco. 
        for person in peaple:
    
            person.user_pass = pws
            person.save()
            return True
    except:
        return False