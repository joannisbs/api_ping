from z_obj_User import (LoginObject)

# Resived Inteface
def R_Userlogin_Interface (data):
    usuario = LoginObject()
    usuario.password = data.get("password")
    usuario.username = data.get("username")
    return usuario

