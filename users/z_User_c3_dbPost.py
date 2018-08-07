from rest_framework import serializers
from users.models import User,Sessionini,HistoryUser

class Post_UserDbSeri (serializers.Serializer):
    id        = serializers.IntegerField(read_only=True)
    user_nome = serializers.CharField(max_length=45)
    user_pass = serializers.CharField(max_length=64)
    user_tipe = serializers.CharField(max_length=1) 

    def Save(self,data):
        try:
            User.objects.create(**data)
            return True
        except:
            return False
            
class Post_SessionDbSeri (serializers.Serializer):
    user_ids   = serializers.IntegerField(default=0)
    token     = serializers.CharField(max_length=64)
    user_tipe = serializers.CharField(max_length=1)   
    ativo     = serializers.BooleanField(default=False)
    horaini   = serializers.IntegerField(default=0)

    def Save(self,data):
        Sessionini.objects.create(**data)
    
class Post_HistoryDbSeri (serializers.Serializer):
    user_ids = serializers.IntegerField(default=0)
    hora     = serializers.CharField(max_length=17)
    event    = serializers.CharField(max_length=100)

    def Save(self,data):
        
        return HistoryUser.objects.create(**data)