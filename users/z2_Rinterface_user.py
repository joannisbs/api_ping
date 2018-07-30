# Imports do Framework:
from rest_framework import serializers

# Imports dos Objetos:
from z_obj_User import ( StandartResponseObject,
                         TokenResponseObject,
                         CreateSessionObject)




# Send Interface

def S_StandardResponse_Interface (sucess,motive):
    response = StandartResponseObject()
    response.sucess = sucess
    response.motive = motive
    response = StandardResponse_Serializer(response)
    return response.data

def S_TokenResponse_Interface (token,status,nivel,ids,user):
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


# Interfaces de Banco

def CreateSessionInterface(tokenSession,person,time):
    response = CreateSessionObject()
    response.token     = tokenSession
    response.ativo     = 1
    response.user_tipe = str(person.user_tipe)
    response.user_ids  = str(person.id)
    response.horaini   = time
    return response