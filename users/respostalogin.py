
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

