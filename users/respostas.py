
class repLog:

    def __init__(self,status,token,nivel,ids,user):
        self.token = token
        self.status = status
        self.nivel = nivel
        self.ids = ids
        self.user = user

class SSession:

    def __init__(self,status,token,nivel,ids,time):
        self.token = token
        self.ativo = status
        self.user_tipe = nivel
        self.user_ids = ids
        self.horaini = time


class Usser:
    def __init__(self,nome,pwd,tipe):
        self.user_nome = nome
        self.user_pass = pwd
        self.user_tipe = tipe
        
class newUser_resp:
    
    def __init__(self, sucess, motive):
        self.sucess = sucess
        self.motive = motive
        ''' Motives, 1 - senhas diferentes
                     2 - usuario ja cadastrado'''
