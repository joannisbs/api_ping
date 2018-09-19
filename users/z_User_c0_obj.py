class LoginObject:
    def __init__(self):
        self.username    = ''
        self.password    = ''

class StandartResponseObject:
    def __init__(self):
        self.sucess      = ''
        self.motive      = ''
    
class TokenResponseObject:
    def __init__(self):
        self.token       = ''
        self.status      = ''
        self.nivel       = ''
        self.ids         = ''
        self.user        = ''
        
class CreateSessionObject:
    def __init__(self):
        self.token       = ''
        self.ativo       = ''
        self.user_tipe   = ''
        self.user_ids    = ''
        self.horaini     = ''

class GetListUserObject:
    def __init__(self):
        self.page        = ''
        self.filtro      = ''
        self.ids         = ''

class Get_ListUsersPersonObject:
    def __init__(self):
        self.ids         = ''
        self.user        = ''
        self.type        = ''

class Get_ListUsersSizeObject:
    def __init__(self):
        self.initpag     = ''
        self.endpag      = ''
        self.size        = ''
        self.next        = ''

class Post_historyUserObject:
    def __init__(self):
        self.user_ids    = ''
        self.hora        = ''
        self.event       = ''
      
class Post_UserObject:
    def __init__(self):
        self.user_nome   = ''
        self.user_pass   = ''
        self.user_tipe   = ''
        self.user_ativo  = ''