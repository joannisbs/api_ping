from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from users.models import User, Sessionini
from Methods import *
from getTime import GetTime
import respostalogin

class UserSerializer (serializers.Serializer):
    id        = serializers.IntegerField(read_only=True)
    user_nome = serializers.CharField(max_length=45)
    user_pass = serializers.CharField(max_length=32)
    user_tipe = serializers.CharField(max_length=1)   

    def Desmonta(self,instance):
        obj = Log()
        obj.user = instance.get('user_nome')
        obj.word = instance.get('user_pass')
        return obj
    
    def Authentic(self, value, psw):
        res = User.objects.filter(user_nome=value)
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
        token = GeraTokenRetorno(psw,time)
        resp = respostalogin.repLog('True',token,nivel,str(ids),user)
        tokenses = GeraTokenSession(token,nivel,user)
        sess = respostalogin.SSession(True,tokenses,nivel,ids,time)
        sess = Session(sess)
        resultado = sess.createSession(sess.data,ids)
        print resultado
        return resp

    def BadLogin(self,user):
        resp = respostalogin.repLog('False','FalhaDeLogin','x','000',user)
        return resp

class RespSerializers(serializers.Serializer):
    token  = serializers.CharField(max_length=64)
    status = serializers.CharField(max_length=6)
    nivel  = serializers.CharField(max_length=1)
    ids    = serializers.CharField(max_length=10)
    user   = serializers.CharField(max_length=45)

class Session(serializers.Serializer):
    user_ids   = serializers.IntegerField(default=0)
    token     = serializers.CharField(max_length=64)
    user_tipe = serializers.CharField(max_length=1)   
    ativo     = serializers.BooleanField(default=False)
    horaini   = serializers.IntegerField(default=0)

    def createSession(self, data, ids):
        res = Sessionini.objects.filter(user_ids=ids,ativo=True)
        for re in res:
            re.ativo = False
            re.save()
        return Sessionini.objects.create(**data)

class Log:
    def __init__(self):
        self.user=''
        self.word=''