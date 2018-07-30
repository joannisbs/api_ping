# Imports da camada de interacao com banco:
from z3_dbGet_User import Get_SizeofListofUsers
from z3_dbGet_User import Get_ListofUsers
from z3_dbGet_User import Get_SessionValid
from z3_dbGet_User import Get_UserActivesForLogin

from z3_dbPost_User import Post_SessionDbSeri 

from z3_dbUpdt_User import Updt_SessiontoInvalid

# Imports de ferramentas:
from z_frame_cript import Cripto_md5, Cripto_sha256
from z_frame_getTime import GetTime

# Imports de interface de resposta
from z2_Rinterface_user import SizeListUser_Serializer 
from z2_Rinterface_user import ListUsers_Serializer 
from z2_Rinterface_user import S_TokenResponse_Interface
from z2_Rinterface_user import CreateSessionInterface
from z2_Rinterface_user import S_StandardResponse_Interface
                                

# Metodos de interacao com a camada de View:
def GetListUser_Method ( data ):
    response = []
    response.append(S_StandardResponse_Interface(True,0))
    try:
        sizeof = Get_SizeofListofUsers(data.page,data.filtro)
        sizeof = SizeListUser_Serializer(sizeof)
        sizeof = sizeof.data

        listofpersons = Get_ListofUsers(data.page,data.filtro)

        if not listofpersons:
            response.append(S_StandardResponse_Interface(False,5))
            return response

        peaple = []
        for item in listofpersons:
            person = ListUsers_Serializer(item)
            peaple.append(person.data)    
    

        response.append(S_StandardResponse_Interface(True,0))
        response.append(sizeof)
        response.append(peaple)
        return response

    except:
        response.append(S_StandardResponse_Interface(False,0))
        return response

def ValidSession_Method ( data ):
    tokenSession = GenerateTokenSessao( str(data.token), str(data.nivel), str(data.ids))    
    session = Get_SessionValid ( data.ids )
    
    if session:
        if session.token == tokenSession:
            time = long(GetTimeMinuts())
            if time - session.horaini > 720:
                Updt_SessiontoInvalid( data.ids )
                return False
            else:
                return True
    return False


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

    response = []
    response.append(S_StandardResponse_Interface(False,3))
    return response    

def ReposnseTokenError():
    response = []
    response.append(S_StandardResponse_Interface(False,3))
    response.append(S_StandardResponse_Interface(False,3))
    response.append(S_StandardResponse_Interface(False,3))
    return response

# Metodos de interacao com outros metodos
def InitSessionofLogin(person):
    time = GetTimeMinuts()
    
    tokenResponse = GenerateTokenResponse( person.user_pass, time)
    tokenSession = GenerateTokenSessao( str(tokenResponse), str(person.user_tipe), str(person.id))
    
    if CreateSession(tokenSession,person,time):
        return tokenResponse
    else:
        return False    

def CreateSession(tokenSession,person,time):
    sessionObject = CreateSessionInterface(tokenSession,person,time)
    session = Post_SessionDbSeri(sessionObject)
    
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

        

