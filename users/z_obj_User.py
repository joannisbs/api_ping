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
        

class CreateSessionObject:
    def __init__(self):
        self.token     = ''
        self.ativo     = ''
        self.user_tipe = ''
        self.user_ids  = ''
        self.horaini   = ''

class GetListUserObject:
    def __init__(self):
        self.page     = ''
        self.filtro   = ''

class Get_ListUsersPersonObject:
    def __init__(self):
        self.ids    = ''
        self.user   = ''
        self.type   = ''

class Get_ListUsersSizeObject:
    def __init__(self):
        self.initpag   = ''
        self.endpag    = ''
        self.size      = ''
        self.next      = ''