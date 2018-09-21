from users.models import Empresas

def Get_CheckIfEmpNameNotExists(name):
    try:
        empresas =  Empresas.objects.filter(emp_nome = name)
        # Existe Apenas um usuario com este nome no banco. 
        for empresa in empresas:
            empresa.number = '=)'
            return True
        return False
    except:
        return False
