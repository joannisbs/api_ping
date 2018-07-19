from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from users.models import User, Sessionini
from Methods import *
from getTime import GetTime
import respostas
import hashlib

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
        resp = respostas.repLog('True',token,nivel,str(ids),user)
        tokenses = GeraTokenSession(token,nivel,user)
        sess = respostas.SSession(True,tokenses,nivel,ids,time)
        sess = Session(sess)
        sess.createSession(sess.data,ids)
        
        return resp

    def BadLogin(self,user):
        resp = respostas.repLog('False','FalhaDeLogin','x','000',user)
        return resp
    
class newUserSerializer(serializers.Serializer):
    user_name = serializers.CharField(max_length=45)
    user_pasw = serializers.CharField(max_length=64)
    user_pasr = serializers.CharField(max_length=64)
    user_tipe = serializers.CharField(max_length=1)  
   
    def createUser(self,data):
        nome = data.get('user_name')
        pswd = data.get('user_pasw')
        pswr = data.get('user_pasr')
        tipe = data.get('user_tipe')
        
        if pswd != pswr:
            return respostas.newUser_resp(False,1) 

        psw= hashlib.md5()
        psw.update(pswd)
        psw = str(psw.hexdigest()) 
        
        person = respostas.Usser(nome,psw,tipe)
        namefind = person.user_nome
        person = UserSerializer(person)
        return self.salvaUser(person.data,namefind)


    def salvaUser(self,data,namefind):
        res = User.objects.filter(user_nome = namefind)
        #return Sessionini.objects.create(**data)
        if len(res)>0:
            return respostas.newUser_resp(False,2) 
        else: 
            User.objects.create(**data)
            return respostas.newUser_resp(True,0) 

class respNewUserSerializers(serializers.Serializer):
    sucess = serializers.BooleanField(default=False)
    motive = serializers.IntegerField(read_only=True)

class RespSerializers(serializers.Serializer):
    token  = serializers.CharField(max_length=64)
    status = serializers.CharField(max_length=6)
    nivel  = serializers.CharField(max_length=1)
    ids    = serializers.CharField(max_length=10)
    user   = serializers.CharField(max_length=45)

    def ValidaSession(self, data):
        ids   = data.get('ids') 
        token = data.get('token')
        nivel = data.get('nivel')
        user  = data.get('user')
        tokenses = GeraTokenSession(token,nivel,user)
        res = Sessionini.objects.filter(user_ids = ids,ativo=True)
        
        t = GetTime()
        time = t.get_TimeInMinuts()
        time = str(time)
        time = long(time)

        for re in res:
            if re.token == tokenses:
                if time - re.horaini > 720:
                    re.ativo = False
                    return False 
                return True
        return False
        

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

