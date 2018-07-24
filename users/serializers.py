from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from users.models import User, Sessionini, History
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
        token = GeraTokenRetorno(psw,time)
        resp = respostas.repLog('True',token,nivel,str(ids),user)
        tokenses = GeraTokenSession(token,nivel,user)
        sess = respostas.SSession(True,tokenses,nivel,ids,time)
        sess = Session(sess)
        sess.createSession(sess.data,ids)
        
        # grava modificacoes
        time = t.get_full_db()
        obj = respostas.objHistory(str(ids),time,"Iniciou a Sessao")
        obj = Historyserial(obj)
        obj.Save(obj.data)
        return resp

    def BadLogin(self,user):
        resp = respostas.repLog('False','FalhaDeLogin','x','000',user)
        return resp
    
class newUserSerializer(serializers.Serializer):
    user_name = serializers.CharField(max_length=45)
    user_pasw = serializers.CharField(max_length=64)
    user_pasr = serializers.CharField(max_length=64)
    user_tipe = serializers.CharField(max_length=1)  
   
    def createUser(self,data,ids):
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

        t = GetTime()
        time = t.get_full_db()
        obj = respostas.objHistory(str(ids),str(time),"Criou o Usuario: " + namefind + " tipo: " +person.user_tipe)
        obj = Historyserial(obj)
        obj.Save(obj.data)

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
                    re.ativo = [False,0]
                    return [False,0] 
                return [True,ids]
        return [False,0]
        

class Session(serializers.Serializer):
    user_ids   = serializers.IntegerField(default=0)
    token     = serializers.CharField(max_length=64)
    user_tipe = serializers.CharField(max_length=1)   
    ativo     = serializers.BooleanField(default=False)
    horaini   = serializers.IntegerField(default=0)


    def createSession(self, data, ids):
        limp = Sessionini.objects.filter(ativo=False)
        for lipr in limp:
            lipr.delete()

        res = Sessionini.objects.filter(user_ids=ids,ativo=True)
        for re in res:
            re.ativo = False
            re.delete()
        return Sessionini.objects.create(**data)

class Log:
    def __init__(self):
        self.user=''
        self.word=''

class Historyserial(serializers.Serializer):
    user_ids = serializers.IntegerField(default=0)
    hora     = serializers.CharField(max_length=17)
    event    = serializers.CharField(max_length=100)

    def Save(self,data):
        return History.objects.create(**data)

def getListUsers(page, filter):
    
    print filter
    number = int(page) * 20
    number1 = number - 20
    
    if filter == "all":
        respo = []
        otherpage = 0
        tamanho = len(User.objects.filter(user_ativo='s'))
        res = User.objects.filter(user_ativo='s').order_by("user_nome")[number1:number]
        if number>tamanho:
            number=tamanho
            otherpage = 1
        respo.append([str(number1+1),str(number),str(tamanho),str(otherpage)])
        for re in res:
            person = [re.id,re.user_nome,re.user_tipe]
            respo.append(person)
        return respo
    else:
        
        respo = []
        otherpage = 0
        tamanho = len(User.objects.filter(user_nome__icontains=filter, user_ativo='s'))
        res = User.objects.filter(user_nome__icontains=filter, user_ativo='s').order_by("user_nome")[number1:number]
        if number>tamanho:
            number=tamanho
            otherpage = 1
        respo.append([str(number1+1),str(number),str(tamanho),str(otherpage)])
        for re in res:
            person = [re.id,re.user_nome,re.user_tipe]
            respo.append(person)
        filter = ''
        return respo