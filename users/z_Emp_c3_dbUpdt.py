from users.models import Empresas

def Updt_DeleteEmp(ids):
    try:
        Emps =  Empresas.objects.filter(id = ids)

        # Existe Apenas um usuario com este nome no banco. 
        for empresa in Emps:
    
            empresa.emp_ativo = False
            empresa.save()
        return True
    except:
        return False

def Updt_ActiveEmp(ids):
    try:
        Emps =  Empresas.objects.filter(id = ids)

        # Existe Apenas um usuario com este nome no banco. 
        for empresa in Emps:
    
            empresa.emp_ativo = True
            empresa.save()
        return True
    except:
        return False