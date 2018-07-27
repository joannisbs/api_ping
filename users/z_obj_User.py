class LoginObject:
    def __init__(self):
        self.username = ''
        self.password = ''

class StandartResponseObject:
    def __init__(self):
        self.sucess = ''
        self.motive = ''
    
class TokenResponseObject:
    def __init__(self):
        self.token  = ''
        self.status = ''
        self.nivel  = ''
        self.ids    = ''
        self.user   = ''
        self.motive = ''

class CreateSessionObject:
    def __init__(self):
        self.token     = ''
        self.ativo     = ''
        self.user_tipe = ''
        self.user_ids  = ''
        self.horaini   = ''