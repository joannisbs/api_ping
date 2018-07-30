from z_obj_User import LoginObject
from z_obj_User import TokenResponseObject
from z_obj_User import GetListUserObject

# Resived Inteface
def R_Userlogin_Interface (data):
    usuario = LoginObject()
    usuario.password = data.get("password")
    usuario.username = data.get("username")
    return usuario

def R_GetTokenfromClient(data):
    response = TokenResponseObject()
    response.ids   = data.get('ids') 
    response.token = data.get('token')
    response.nivel = data.get('nivel')
    response.user  = data.get('user')
    return response

def R_GetListUser_Interface( data ):
    response = GetListUserObject()
    response.page   = data.get('page') 
    response.filtro = data.get('filtro')
    return response