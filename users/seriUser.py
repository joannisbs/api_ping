from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from users.models import User
from getTime import GetTime
from respostas import Resposta_padrao
import respostas
import hashlib
import seriMethodos
from seriSessao import Session

class UserSerializer (serializers.Serializer):
    id        = serializers.IntegerField(read_only=True)
    user_nome = serializers.CharField(max_length=45)
    user_pass = serializers.CharField(max_length=64)
    user_tipe = serializers.CharField(max_length=1)   

    def Desmonta(self,instance):
        obj = Log()
        obj.user = instance.get('user_nome')
        obj.word = instance.get('user_pass')
        return obj
    
    def Authentic(self, value, psw):
        #ALTERAR FALHA DE LOGIN
        res = User.objects.filter(user_nome=value,user_ativo='s')|User.objects.filter(user_nome=value,user_ativo='A')
        for re in res:
            pswli =  re.user_pass
        if pswli == psw:
            return [True,re.user_tipe,re.id]
        else:
            return [False,'nothing',0]

    def IniciaSessao(self,psw,nivel,ids,user):
        t = GetTime()
        time = t.get_TimeInMinuts()
        time = str(time)
        token = seriMethodos.GeraTokenRetorno(psw,time)
        resp = respostas.repLog('True',token,nivel,str(ids),user)
        tokenses = seriMethodos.GeraTokenSession(token,nivel,user)
        sess = respostas.SSession(True,tokenses,nivel,ids,time)
        sess = Session(sess)
        sess.createSession(sess.data,ids)
        return resp

    def BadLogin(self,user):
        resp = respostas.repLog('False','FalhaDeLogin','x','000',user)
        return resp

def DeleteUsuario(ids):
    resp = Resposta_padrao(False,"1")
    res = User.objects.filter(id=ids)
    for re in res:
        re.user_ativo = 'n'
        re.save()
        resp = [True,"0"]
    
    return resp


def GetUserById(ids):
    res = User.objects.filter(id=ids)
    for re in res:
        return re.user_nome

class Log:
    def __init__(self):
        self.user=''
        self.word=''