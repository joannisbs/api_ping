# Imports do Framework:
from rest_framework import serializers

# Imports dos Objetos:
from z_User_c0_obj import Post_UserObject
from z_User_c0_obj import TokenResponseObject
from z_User_c0_obj import CreateSessionObject
from z_User_c0_obj import StandartResponseObject

# Send Modal

def S_StandardResponse_Modal (sucess,motive):
    response = StandartResponseObject()
    response.sucess = sucess
    response.motive = motive
    response = StandardResponse_Serializer(response)
    return response.data

def S_TokenResponse_Modal (token,status,nivel,ids,user):
    response = TokenResponseObject()
    
    response.token  = token
    response.status = status
    response.nivel  = nivel
    response.ids    = ids
    response.user   = user
    
    response = TokenResponse_Serializer(response)
    return response.data

# Serializers

class StandardResponse_Serializer(serializers.Serializer):
    sucess = serializers.BooleanField(default=False)
    motive = serializers.CharField(max_length=1)

class TokenResponse_Serializer(serializers.Serializer):
    token  = serializers.CharField(max_length=64)
    status = serializers.CharField(max_length=6)
    nivel  = serializers.CharField(max_length=1)
    ids    = serializers.CharField(max_length=10)
    user   = serializers.CharField(max_length=45)

class SizeListUser_Serializer(serializers.Serializer):
    initpag = serializers.CharField(max_length=6)
    endpag  = serializers.CharField(max_length=6)
    size    = serializers.CharField(max_length=6)
    next    = serializers.CharField(max_length=1)

class ListUsers_Serializer(serializers.Serializer):
    ids  = serializers.CharField(max_length=10)
    user = serializers.CharField(max_length=45)
    type = serializers.CharField(max_length=1)

class ListHistoryUsers_Serializer(serializers.Serializer):
    hora     = serializers.CharField(max_length=17)
    event    = serializers.CharField(max_length=100)

class User_Serializer(serializers.Serializer):
    user_nome = serializers.CharField(max_length=45)
    user_pass = serializers.CharField(max_length=32)
    user_tipe = serializers.CharField(max_length=1)
    user_ativo = serializers.CharField(max_length=1)  
    
# Modals de Banco

def CreateSession_Modal(tokenSession,person,time):
    response = CreateSessionObject()
    response.token     = tokenSession
    response.ativo     = 1
    response.user_tipe = str(person.user_tipe)
    response.user_ids  = str(person.id)
    response.horaini   = time
    return response

def CreateUser_Modal(login,tipe):
    response = Post_UserObject()
    response.user_ativo = 's'
    response.user_pass  = "dd6e5e5918e94d997c686fcebc56922f"
    response.user_nome  = login
    response.user_tipe  = tipe

    return response