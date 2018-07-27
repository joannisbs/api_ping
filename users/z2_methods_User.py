# Imports da camada de interacao com banco:
from z3_dbGet_User import Get_UserActivesForLogin
from z3_dbPost_User import SessionDbSeri

# Imports de ferramentas:
from z_frame_cript import Cripto_md5, Cripto_sha256
from z_frame_getTime import GetTime

# Imports de interface de resposta
from z2_Rinterface_user import (S_StandardResponse_Interface,
                                S_TokenResponse_Interface,
                                CreateSessionInterface)

# Metodos de interacao com a camada de View:

def Userlogin_Method ( data ):
    person = Get_UserActivesForLogin ( data.username )
    md5_Password = Cripto_md5 ( data.password )
    
    if person:

        if md5_Password == person.user_pass:
            tokenResponse = InitSessionofLogin( person )
            if tokenResponse:
                
                response = []
                response.append(S_StandardResponse_Interface(True,0))
                
                token = S_TokenResponse_Interface (tokenResponse,
                                                    "True",
                                                    person.user_tipe,
                                                    person.id,
                                                    person.user_nome)
                response.append(token)
                return response 
            
            else:
                response = []
                response.append(S_StandardResponse_Interface(False,3))
                return response
        else:
            response = []
            response.append(S_StandardResponse_Interface(False,3))
            return response
    else:
        response = []
        response.append(S_StandardResponse_Interface(False,3))
        return response
        

# Metodos de interacao com outros metodos
def InitSessionofLogin(person):
    time = GetTimeMinuts()
    
    tokenResponse = GenerateTokenResponse( person.user_pass, time)
    tokenSession = GenerateTokenSessao( tokenResponse, person.user_tipe, str(person.id))
    
    if CreateSession(tokenSession,person,time):
        return tokenResponse
    else:
        return False


    

def CreateSession(tokenSession,person,time):
    sessionObject = CreateSessionInterface(tokenSession,person,time)
    session = SessionDbSeri(sessionObject)
    
    try:
        session.Save(session.data)
        return True
    except:
        return False


# Metodos Secundarios
def GetTimeMinuts():
    t = GetTime()
    time = t.get_TimeInMinuts()
    return time

def GenerateTokenResponse(psw,time):
    string = psw + time
    token = Cripto_sha256(string)
    return token

def GenerateTokenSessao(token,nivel,user):
    string = token + nivel + user
    token = Cripto_sha256(string)
    return token

        

