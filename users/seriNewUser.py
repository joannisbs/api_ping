from rest_framework import serializers
from users.seriUserHistory import CriaHistorico
from users.Methods import decodificatipodeconta
from users.seriUser import UserSerializer
from users.models import User
import respostas
import hashlib
from getTime import GetTime

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

        tipoConta = decodificatipodeconta(person.user_tipe)

        
        person = UserSerializer(person)
        return self.salvaUser(person.data,namefind,tipoConta)


    def salvaUser(self,data,namefind,tipoConta):
        res = User.objects.filter(user_nome = namefind)
        #return Sessionini.objects.create(**data)
        if len(res)>0:
            return respostas.newUser_resp(False,2) 
        else: 
            User.objects.create(**data)
            string = "Criou o Usuario: " + str(namefind) + " tipo: " + str(tipoConta)
            CriaHistorico(str(ids),string)
            return respostas.newUser_resp(True,0) 

class respNewUserSerializers(serializers.Serializer):
    sucess = serializers.BooleanField(default=False)
    motive = serializers.IntegerField(read_only=True)
