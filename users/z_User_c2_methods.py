# Imports da camada de interacao com banco:
from z_User_c3_dbGet import Get_SizeofListofUsers
from z_User_c3_dbGet import Get_ListofUsers
from z_User_c3_dbGet import Get_SessionValid
from z_User_c3_dbGet import Get_UserActivesForLogin
from z_User_c3_dbGet import Get_UserById
from z_User_c3_dbGet import Get_ListofHistoryUsers
from z_User_c3_dbGet import Get_SizeHistoryofUsers
from z_User_c3_dbGet import Get_checkUserExists
from z_User_c3_dbGet import Get_UserIdbyName

from z_User_c3_dbPost import Post_SessionDbSeri 
from z_User_c3_dbPost import Post_HistoryDbSeri 
from z_User_c3_dbPost import Post_UserDbSeri

from z_User_c3_dbUpdt import Updt_SessiontoInvalid
from z_User_c3_dbUpdt import Updt_DeleteUser
from z_User_c3_dbUpdt import Updt_ReactivateUser
from z_User_c3_dbUpdt import Updt_ResetUser
from z_User_c3_dbUpdt import Updt_AlterTypeUser
from z_User_c3_dbUpdt import Updt_NewPass 

# Imports de ferramentas:
from z__frame_cript import Cripto_md5, Cripto_sha256
from z__frame_getTime import GetTime
from z_User_c0_obj import Post_historyUserObject
from z__functionsgenericas import RetornaType

# Imports de interface de resposta
from z_User_c2_modals import SizeListUser_Serializer 
from z_User_c2_modals import ListUsers_Serializer 
from z_User_c2_modals import ListHistoryUsers_Serializer 
from z_User_c2_modals import CreateUser_Modal
from z_User_c2_modals import S_TokenResponse_Modal
from z_User_c2_modals import CreateSession_Modal

from z_User_c2_modals import S_StandardResponse_Modal

# Metodos de interacao com a camada de View:
def CreateUser_Method (id_user,login,TypesOfAccont):
    response = CreateUser_Modal (login,TypesOfAccont)
    if Get_checkUserExists(login):
        if Post_UserDbSeri(response):
            response = Post_UserDbSeri(response)
            response.Save(response.data)
            tipo = RetornaType(TypesOfAccont) 
            idcriado = Get_UserIdbyName(login)
            nomedocriador = Get_UserById(id_user)
            InsertHistoryUser (idcriado,
                        "Criado por: " + nomedocriador + " tipo: " + tipo)
            InsertHistoryUser (id_user,
                        "Criou o usuario: " + login + " tipo: " + tipo)
            return 1
        else:
            return '5'
    else:
        return '4'

def AlterTypeUser_Method ( id_user, ids, types  ):
    try:
        if Updt_AlterTypeUser( int(ids), types ):
            name = Get_UserById(int(ids) )
            tipo = RetornaType(types) 
            nomeAlterador = Get_UserById(int(id_user) )
            InsertHistoryUser (id_user,
                        "Alterou o usuario: " + name + " para o tipo: " + tipo)

            InsertHistoryUser (int(ids),
                        "Alterado tipo por: " + nomeAlterador + " para: " + tipo)
            return True
        return False
    except:
        return False
    return False
def NewPass_Method ( id_user, pws):
    pwd = Cripto_md5(pws)
    try:
        if Updt_NewPass( int(id_user) , pwd ):
            InsertHistoryUser(id_user,"Trocou a propria senha")
            return True
        return False
    except:
        return False
    return False
                   
def ResetUser_Method ( id_user, ids  ):
    try:
        if Updt_ResetUser( int(ids) ):
            name = Get_UserById(int(ids) )
            InsertHistoryUser(id_user,"Resetou a senha do usuario: "+ name)

            nomeAlterador = Get_UserById(int(id_user) )

            InsertHistoryUser (int(ids),
                        "Senha resetada por: " + nomeAlterador)

            return True
        return False
    except:
        return False
    return False
                         
def Reactivate_user_Method ( id_user, ids ):
    try:
        if Updt_ReactivateUser( int(ids) ):
            name = Get_UserById(int(ids) )
            InsertHistoryUser(id_user,"Reativou o usuario: "+ name)
            nomeAlterador = Get_UserById(int(id_user) )
            InsertHistoryUser (int(ids),
                        "Conta reativada por: " + nomeAlterador)
            return True
        return False
    except:
        return False
    return False

def DeleteUser_Method ( id_user, ids ):
    try:
        if Updt_DeleteUser( int(ids) ):
            name = Get_UserById(int(ids) )
            InsertHistoryUser(id_user,"Desativou o usuario: "+ name)
            nomeAlterador = Get_UserById(int(id_user) )
            InsertHistoryUser (int(ids),
                        "Conta desativada por: " + nomeAlterador)
            return True
        return False
    except:
        return False
    return False


        
def GethistoryUser_Method (  ids, page,filtro ):
    response = []
    filtro = ArrumaData(filtro)
    response.append(S_StandardResponse_Modal(True,0))
    try:
        sizeof = Get_SizeHistoryofUsers(ids, page,filtro)
        sizeof = SizeListUser_Serializer(sizeof)
        sizeof = sizeof.data

        listofhistory = Get_ListofHistoryUsers(ids, page,filtro)
        
        if not listofhistory:
            response.append(S_StandardResponse_Modal(False,5))
            return response
            
        peaple = []
        for item in listofhistory:
            person = ListHistoryUsers_Serializer(item)
            peaple.append(person.data)    
            

        response.append(S_StandardResponse_Modal(True,0))
        response.append(sizeof)
        response.append(peaple)
        return response

    except:
        response.append(S_StandardResponse_Modal(False,0))
        return response

def GetListUser_Method ( data ,condicion):
    response = []
    response.append(S_StandardResponse_Modal(True,0))
    try:
        sizeof = Get_SizeofListofUsers(data.page,data.filtro,condicion)
        sizeof = SizeListUser_Serializer(sizeof)
        sizeof = sizeof.data

        listofpersons = Get_ListofUsers(data.page,data.filtro,condicion)

        if not listofpersons:
            response.append(S_StandardResponse_Modal(False,5))
            return response

        peaple = []
        for item in listofpersons:
            person = ListUsers_Serializer(item)
            peaple.append(person.data)    
    

        response.append(S_StandardResponse_Modal(True,0))
        response.append(sizeof)
        response.append(peaple)
        return response

    except:
        response.append(S_StandardResponse_Modal(False,0))
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
                response.append(S_StandardResponse_Modal(True,0))
                
                token = S_TokenResponse_Modal (tokenResponse,
                                                    "True",
                                                    person.user_tipe,
                                                    person.id,
                                                    person.user_nome)
                response.append(token)
                return response 
            
            else:
                response = []
                response.append(S_StandardResponse_Modal(False,3))
                return response
        else:
            response = []
            response.append(S_StandardResponse_Modal(False,3))
            return response
    else:
        response = []
        response.append(S_StandardResponse_Modal(False,3))
        return response

    response = []
    response.append(S_StandardResponse_Modal(False,3))
    return response   

def ResponseStandart(condicion):
    if condicion:
        return S_StandardResponse_Modal(True,0)
    return S_StandardResponse_Modal(False,3)

def ResponseStandartWithMotive(condicion,motive):
    if condicion:
        return S_StandardResponse_Modal(True,0)
    return S_StandardResponse_Modal(False,motive)

def ReposnseTokenError():
    response = []
    response.append(S_StandardResponse_Modal(False,3))
    response.append(S_StandardResponse_Modal(False,3))
    response.append(S_StandardResponse_Modal(False,3))
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
    sessionObject = CreateSession_Modal(tokenSession,person,time)
    session = Post_SessionDbSeri(sessionObject)
    
    try:
        session.Save(session.data)
        return True
    except:
        return False

def InsertHistoryUser(user,hystory):
    histo = Post_historyUserObject()
    time = GetTimeDB()
    histo.user_ids = user
    histo.hora = time
    histo.event = hystory
    histo = Post_HistoryDbSeri(histo)
    histo.Save(histo.data)

    #Post_HistoryDbSeri
# Metodos Secundarios
def GetTimeMinuts():
    t = GetTime()
    time = t.get_TimeInMinuts()
    return time

def GetTimeDB():
    t = GetTime()
    time = t.get_full_db()
    return time

def GenerateTokenResponse(psw,time):
    string = psw + time
    token = Cripto_sha256(string)
    return token

def GenerateTokenSessao(token,nivel,user):
    string = token + nivel + user
    token = Cripto_sha256(string)
    return token

        
def ArrumaData(data):
    dataarrumada = data
    if '/' in data:
        dado = data.split('/')
        if len(dado) == 3:
            if len(dado[2])==1:
                dado[2] = ''
            if len(dado[0])==1:
                dado[0] = '0' + dado[0]
            if len(dado[2])==3:
                dado[2] = ''
            if len(dado[2])==4:
                dado[2] = dado[2][2] + dado[2][3]
            dataarrumada = dado[2] + "_" + dado[1] + "_" + dado [0]
        elif len(dado) == 2:
            if len(dado[1])==1:
                dado[1] = ''
            if len(dado[0])==1:
                dado[0] = '0' + dado[0]
            dataarrumada = dado[1] + "_" + dado [0]
        else:
            dataarrumada = data

    return dataarrumada        

