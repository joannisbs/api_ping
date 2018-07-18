from rest_framework import serializers
from users.models import User
from Methods import *
from getTime import GetTime

class UserSerializer (serializers.Serializer):
    id        = serializers.IntegerField(read_only=True)
    user_nome = serializers.CharField(max_length=45)
    user_pass = serializers.CharField(max_length=32)
    user_tipe = serializers.CharField(max_length=1)   

    def Desmonta(self,instance):

        instance.user = instance.get('user')
        instance.word = instance.get('pass')
        return instance
    
    def Authentic(self, value, psw):
        res = User.objects.filter(user_nome=value)
        for re in res:
            pswli =  re.user_pass
        if pswli == psw:
            return [True,re.user_tipe,re.id]
        else:
            return [False,'nothing',0]

    def IniciaSessao(self,psw,nivel,id):
        t = GetTime()
        time = t.get_TimeInMinuts
        time = str(time)
        token = GeraTokenRetorno(psw,time)

        StringRet = "Status:True,Token:" + token
        StringRet = StringRet + ",Nivel:" + nivel
        StringRet = StringRet + ",Id:" + str(id)
        return StringRet

