from z_obj_User import LoginObject
from z_obj_User import TokenResponseObject

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