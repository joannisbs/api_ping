from rest_framework import serializers
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

        t = GetTime()
        time = t.get_full_db()
        tipoConta = decodificatipodeconta(person.user_tipe)
        obj = respostas.objHistory(str(ids),str(time),"Criou o Usuario: " + namefind + " tipo: " + tipoConta)
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
